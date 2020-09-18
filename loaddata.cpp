#include "boost/python/numpy.hpp"
#include <stdexcept>
#include <algorithm>

namespace p = boost::python;
namespace np = boost::python::numpy;

#include <iostream>
#include <fstream>
#include <stdio.h>
#include <string.h>
#include <vector>
using namespace std;

#define IMG_SIZE 256

vector<string> split(string str, char del) {
    int first = 0;
    int last = str.find_first_of(del);
    vector<string> result;
    if(last < 0) return result;
 
    while (first < str.size())
    {
        string subStr(str, first, last - first);
 
        result.push_back(subStr);
 
        first = last + 1;
        last = str.find_first_of(del, first);
 
        if (last == string::npos) {
            last = str.size();
        }
    }
 
    return result;
}

np::ndarray read_images(string filename, int output_size, int channel)
{
    cout << "reading image..." << endl;
    ifstream ifs(filename, ios::binary);
    if(!ifs.is_open())
    {
        cout << "cannot open: " << filename << endl;
    }
    unsigned long output_size_ = output_size;
    unsigned long channel_ = channel;
    vector<double> Images(output_size_*IMG_SIZE*IMG_SIZE*channel);
    unsigned long counter = 0;
    while(!ifs.eof())
    {
        cout << "\r" << "reading image " << counter << "/" << output_size << std::string(20, ' ');
        string line;
        getline(ifs, line);
        if(line.length() <= 1)
        {
            break;
        }
        vector<string> vals = split(line, ',');
        for(int i = 0; i < IMG_SIZE*IMG_SIZE*channel_; i++)
        {
            Images[counter*IMG_SIZE*IMG_SIZE*channel_ + i] = stof(vals[i + 1])/255.0; //127.5 - 1.0;
        }
        if(counter == output_size_ - 1) break;
        else counter++;
    }
    cout << endl;
    ifs.close();
    
    Py_intptr_t shape[4] = {output_size, IMG_SIZE, IMG_SIZE, channel};
    np::ndarray result = np::zeros(4, shape, np::dtype::get_builtin<double>());
    std::copy(Images.begin(), Images.end(), reinterpret_cast<double*>(result.get_data()));
    return result;
}

BOOST_PYTHON_MODULE(libloaddata){
    Py_Initialize();
    np::initialize();
    p::def("read_images", read_images);
}
