
#include <iostream>
#include <iomanip>
#include <assert.h>
#include <opencv2/core.hpp>
#include <opencv2/highgui.hpp>
#include <opencv2/imgproc.hpp>
#include <opencv2/core/utility.hpp>
#include "dirent.h"
#include "browser.hpp"
#include "dir.cpp"
#include "dir.h"

#ifdef _WIN32
#include <Windows.h>
#endif

using namespace cv;
using namespace std;

int maxcols;	//!< Default max number of columns to show
int maxrows;	//!< Default max number of rows to show

int searchDir(const char* path, vector<string>& vPaths);

/******************************************************************************
 * \brief Display the specified image.
 *
 * Display the image specified in the argument.  This function ensures that the
 * image will fit in the windows, while maintaining the aspect ratio.
 *
 * @param [in] Image to be displayed
 * \return Key pressed by the user
 *****************************************************************************/

uchar display(const Mat& img)
{
	// TO DO
	return (0);
}


int main( int argc, const char ** argv )
{
	vector<string> paths;
    vector<string> finalPaths;
	Mat image;
    DIR* dir;
    DIR* dirCheck;


	try
	{
		// parse the command line arguments

		CommandLineParser parser(argc, argv, keys);
		string dir = parser.get<string>(0);

		parser.about("Image Browser v1.0");
		if (parser.has("help") || dir.empty() )
		{
			parser.printMessage();
			return (1);
		}

		if (parser.has("r") || parser.has("rows")){
			maxrows = parser.get<int>("r");
		}

		if (parser.has("c") || parser.has("cols")){
			maxcols = parser.get<int>("c");
		}

		if (!parser.check()){
			parser.printErrors();
			return 1;
		}

		String path1 = parser.get<String>("directory");
		const char* path = path1.c_str();

		if ((dirCheck = opendir(path)) == NULL){
			perror("opendir() error");
		}
		else{

		}

	}
	catch (string& str)				// Handle string exception
	{
		cerr << "Error: " << argv[0] << ": " << str << endl;
		return (1);
	}
	catch (Exception& e)				// Handle OpenCV exception
	{
		cerr << "Error: " << argv[0] << ": " << e.msg << endl;
		return (1);
	}
	return (0);
}