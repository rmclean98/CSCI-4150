#include <iostream>
#include <opencv2/
#include <opencv2/highgui.hpp>

using namespace cv;
using namespace std;

void callback(int state, void*userData) {
    cout << "hey" << endl;
    // do something
}

int main(int argc, char *argv[])
{
    namedWindow("main1",WINDOW_NORMAL);

createButton("",callback);//create a push button "button 0", that will call callbackButton.

    Mat img1 = imread("/Users/ryanmclean/Documents/School/CSCI-4150/Images");

    while( waitKey(33) != 27 )
    {
        imshow("main1",img1);

    }
    destroyAllWindows();
    return 0;
}
