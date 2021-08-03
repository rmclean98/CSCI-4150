#include <iostream>
#include <iomanip>
#include <vector>
#include <assert.h>
#include <opencv2/core.hpp>
#include <opencv2/highgui.hpp>
#include <opencv2/imgproc.hpp>
#include <opencv2/core/utility.hpp>
#include <sys/stat.h>
#include "dirent.h"
#ifdef _WIN32
#include <Windows.h>
#endif


using namespace cv;
using namespace std;


int searchDir(String path, vector<string>& vPaths);

int TransformImage(Mat original, Mat image1, Mat image2, int resizeNum, int intensityChange);

int main(int argc, char* argv[]) {

    bool unixOS = true;

    vector<string> paths;
    vector<string> finalPaths;
    Mat image;
    Mat image1;
    Mat image2;
    DIR* dir;
    DIR* dirCheck;


    //Parameters for OpenCV's CommandLineParser
    const String keys =
        "{help h usage ? || Shows help}"
        "{@dir           ||input directory}"
        ;

    CommandLineParser parser(argc, argv, keys);
    parser.about("Image Browser v1");

    if (argc == 1 || parser.has("help")) {
        parser.printMessage();
        return 0;
    }

    if (!parser.check())
    {
        parser.printErrors();
        return 0;
    }

    String path = parser.get<String>(0);
    const char* path1 = path.c_str();

    if ((dirCheck = opendir(path1)) == NULL) {
        perror("opendir() error");
    }
    else {
        searchDir(path, paths);
        int pathSize = paths.size();
        //cout << pathSize << endl;
        int removeFileCount = 0;


        if (pathSize > 0) {
            for (int i = 0; i < pathSize; i++) {
                //cout << "Total Files: " << pathSize << " File Count: " << i << " path: " << paths.at(i) << endl;
                image = imread(paths.at(i), IMREAD_COLOR);
                //cout << image.empty() << endl;
                if (!image.empty()) {
                    finalPaths.push_back(paths.at(i));
                }
            }

            int totalFiles = finalPaths.size();

            image = imread(finalPaths.at(0), IMREAD_COLOR);
            image1 = imread(finalPaths.at(1), IMREAD_COLOR);
            image2 = imread(finalPaths.at(2), IMREAD_COLOR);

            if((image.cols * image.rows) > (image1.cols * image1.rows)){
                Mat temp;
                temp = image;
                image = image1;
                image1 = temp;
            }
            if((image1.cols * image1.rows) > (image2.cols * image2.rows)){
                Mat temp;
                temp = image1;
                image1 = image2;
                image2 = temp;
            }

            int resizeNum = 4;
            int intensityChange = 0;
            int lastNum = 1;

            if (totalFiles > 0) {
                char userInput;
                for (; ;) {
                    if (!finalPaths.empty()) {

                        if (lastNum != resizeNum){
                          lastNum = TransformImage(image, image1, image2, resizeNum, intensityChange);
                        }

                        userInput = waitKey(0);

                        if (userInput == 113) {
                            break;
                        }
                        else if (userInput == 110 || userInput == 32) {
                            resizeNum++;
                            if (resizeNum > 2) {
                                resizeNum = 0;
                            }
                        }
                        else if (userInput == 112) {
                            resizeNum--;
                            if (resizeNum < 0) {
                                resizeNum = 2;
                            }
                        }
                    }
                }
            }

        }
        else
        {
            cout << "No Images available in the given directory.";
        }
    }
    return 0;
}


int TransformImage(Mat original, Mat image1, Mat image2, int resizeNum, int intensityChange) {

  destroyAllWindows();
  Mat originalImage = original;
  Mat resized1 = image1;
  Mat resized2 = image2;


  Size originalSize = originalImage.size();

  String window_name = "original";
  namedWindow(window_name);
  imshow(window_name, originalImage);
  String window_name1;
  String window_name2;

  cout << "Original: " << originalImage.rows << "x" << originalImage.cols << endl;
  cout << "Medium: " << resized1.rows << "x" << resized1.cols << endl;
  cout << "large: " << resized2.rows << "x" << resized2.cols << endl;

  namedWindow(window_name1);
  imshow("Original med", resized1);
  namedWindow(window_name2);
  imshow("Original large", resized2);

  if(resizeNum == 0){
    String window_name1 = "Image_Nearest_neighbour, Medium";
    String window_name2 = "Image_Nearest_neighbour, Large";
    //resize(image1, resized1, originalSize, 0, 0, INTER_NEAREST);
    namedWindow(window_name1);
    imshow(window_name1, resized1);
    //resize(image2, resized2, originalSize, 0, 0, INTER_NEAREST);
    namedWindow(window_name2);
    imshow(window_name2, resized2);
  }else if(resizeNum == 1){
    String window_name1 = "Image_BiLinear, Medium";
    String window_name2 = "Image_BiLinear, Large";
    resize(image1, resized1, originalSize, 0, 0, INTER_LINEAR);
    //namedWindow(window_name1);
    imshow(window_name1, resized1);
    //resize(image2, resized2, originalSize, 0, 0, INTER_LINEAR);
    namedWindow(window_name2);
    imshow(window_name2, resized2);
  }else if(resizeNum == 2){
    String window_name1 = "Image_BiCubic, Medium";
    String window_name2 = "Image_BiCubic, Large";
    resize(image1, resized1, originalSize, 0, 0, INTER_CUBIC);
    namedWindow(window_name1);
    imshow(window_name1, resized1);
    resize(image2, resized2, originalSize, 0, 0, INTER_CUBIC);
    namedWindow(window_name2);
    imshow(window_name2, resized2);
  }


  String window_IntensityChange = "window_IntensityChange";

  return resizeNum;

}


int searchDir(String path, vector<string>& vpaths) {

    const char* tempPath1 = path.c_str();
    DIR* dir = opendir(tempPath1);
    struct dirent* ent;
    const char* tempPath;
    string tmp;
    string ntmp;

    if (!dir)
        return 1;

    while ((ent = readdir(dir)) != NULL) {
        struct stat file_info;
        stat(ent->d_name, &file_info);

        if (ent->d_type == DT_REG) {

#ifdef _WIN32
            tmp = path + "\\" + (ent->d_name);
#else
            tmp = path + "/" + (ent->d_name);
#endif
            vpaths.push_back(tmp);

        }
#ifdef __linux
        else if (S_ISDIR(file_info.st_mode)) {
            if (strcmp(ent->d_name, ".") != 0 && strcmp(ent->d_name, "..") != 0) {
#else
        else if (ent->d_type == DT_DIR && strcmp(ent->d_name, ".") && strcmp(ent->d_name, "..")) {
#endif

#ifdef _WIN32
            tmp = path + "\\" + (ent->d_name);
#else
            tmp = path + "/" + (ent->d_name);
            cout << tmp << endl;
#endif
            searchDir(tmp, vpaths);

#ifdef __linux
        }
            }
#else
        }
#endif


    }
    closedir(dir);

}
