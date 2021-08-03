#include "opencv2/imgproc/imgproc.hpp"
#include "opencv2/highgui/highgui.hpp"

using namespace std;
using namespace cv;

Mat src; 
Mat dst;

char window_name1[] = "Original image";
char window_name2[] = "Blurred image";

int main( int argc, char** argv )
{
    /// load the source image
    src = imread( argv[1], 1 );

    namedWindow( window_name1, WINDOW_AUTOSIZE );
    imshow("Original image",src);

    dst = src.clone();
    GaussianBlur( src, dst, Size( 15, 15 ), 0, 0 );

    namedWindow( window_name2, WINDOW_AUTOSIZE );
    imshow("Blurred image", dst);

    waitKey();
    return 0;
}