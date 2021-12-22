#include "01-opencv-시작하기.hpp"

void open_multiple_images() {
    const char *path = "your image path";
    
    std::vector<std::string> filenames;
    cv::glob(path, filenames, true);
    
    for (int idx=0; idx < filenames.size(); idx++)
    {
        std::string filename = filenames[idx];
        
        cv::Mat input = cv::imread(filename);
        
        cv::imshow("img", input);
        cv::waitKey(0);
    }
}

void slide_show() {
    const char *path = "your image path";
    
    std::vector<std::string> filenames;
    cv::glob(path, filenames, true);
    
    int idx = 0;
    int cnt = filenames.size();
    
    while (true) {
        cv::Mat img = cv::imread(filenames[idx]);
        cv::imshow("img", img);
        
        if (cv::waitKey(1000) >= 0) {
            break;
        }
        
        idx += 1;
        if (idx >= cnt) {
            idx = 0;
        }
    }
    
    cv::destroyAllWindows();
}