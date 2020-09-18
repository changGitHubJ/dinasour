#include <iostream>
#include <fstream>
#include <vector>
#include <random>
#include <sys/stat.h>
using namespace std;

#define TRAIN_DATA_SIZE0 100
#define TRAIN_DATA_SIZE1 300
#define TEST_DATA_SIZE 50
#define SHUFFLE false

int randint(int min, int max)
{
    int width = max - min + 1;
    std::random_device rnd; // 非決定的な乱数生成器でシード生成機を生成
    std::mt19937 mt(rnd()); //  メルセンヌツイスターの32ビット版、引数は初期シード
    std::uniform_int_distribution<> rand9999(0, 9999*width); // [0, 9999*width] 範囲の一様乱数
    int randi = rand9999(mt);
    int val = min + randi/10000;
    return val;
}

int main(int argc, char* argv[])
{
    vector<string> directories;
    directories.push_back("images/tyrannosaurus/");
    directories.push_back("images/triceratops/");
    directories.push_back("images/brachiosaurus/");
    directories.push_back("images/stegosaurus/");
    directories.push_back("images/iguanodon/");
    directories.push_back("images/ornithomimus/");
    directories.push_back("images/pteranodon/");

    vector<string> testImage;
    vector<string> trainImage0;
    vector<string> trainImage1;
    for(int i = 0; i < 7; i++) // category
    {
        vector<int> indices;
        for(int j = 0; j < 500; j++)
        {
            indices.push_back(j);
        }
        //int counter = 0;
        int counter_f = 0;
        int counter_train = 0;
        int counter_test = 0;
        string filename = "";
        bool test = false;
        bool test_complete = false;
        while(true) // image
        {
            if(SHUFFLE)
            {
                int num = randint(0, indices.size() - 1);
                filename = directories[i] + to_string(indices[num]) + "_256.txt";
                indices.erase(indices.begin() + num);
            }
            else
            {
                filename = directories[i] + to_string(counter_f) + "_256.txt";
                counter_f++;
            }
            ifstream ifs(filename);
            if(!ifs.is_open())
            {
                cout << "not found: " << filename << endl;
                continue;
            }
            
            string line = ""; //to_string(counter);
            while(!ifs.eof())
            {
                string buf;
                getline(ifs, buf);
                if(buf.length() > 0)
                {
                    line += "," + buf;
                }
                else
                {
                    break;
                }
            }
            line += "\n";
            ifs.close();
            
            if(!test || test_complete)
            {
                cout << filename << ", counter_train = " << counter_train << endl;
                if(counter_train < TRAIN_DATA_SIZE0)
                {
                    trainImage0.push_back(to_string(counter_train) + line);
                    trainImage1.push_back(to_string(counter_train) + line);
                    counter_train++;
                    test = true;
                }
                else
                {
                    trainImage1.push_back(to_string(counter_train) + line);
                    counter_train++;
                    test = true;
                }
                if(counter_train >= TRAIN_DATA_SIZE1) break;
            }
            else
            {
                cout << filename << ", counter_test = " << counter_test << endl;
                testImage.push_back(to_string(counter_test) + line);
                counter_test++;
                test = false;
                if(counter_test >= TEST_DATA_SIZE)
                {
                    test_complete = true;
                }
            }
            
            // if(counter < TEST_DATA_SIZE)
            // {
            //     
            // }
            // else if(counter < TEST_DATA_SIZE + TRAIN_DATA_SIZE0)
            // {
            //     trainImage0.push_back(line);
            //     trainImage1.push_back(line);
            //     counter++;
            // }
            // else
            // {
            //     trainImage1.push_back(line);
            //     counter++;
            // }
            // if(counter >= TEST_DATA_SIZE + TRAIN_DATA_SIZE1) break;
        }
    }
     
    struct stat statBuf;
    mode_t mode;
    mode = S_IRWXU | S_IRGRP | S_IXGRP | S_IROTH | S_IXOTH;
    if(stat("./data", &statBuf) != 0)   
    {
        mkdir("./data", mode);
    }
    string test = "";
    string train_100 = "";
    string train_300 = "";
    if(SHUFFLE)
    {
        test = "./data/testImage256_shuffle.txt";
        train_100 = "./data/trainImage256_100_shuffle.txt";
        train_300 = "./data/trainImage256_300_shuffle.txt";
    }
    else
    {
        test = "./data/testImage256.txt";
        train_100 = "./data/trainImage256_100.txt";
        train_300 = "./data/trainImage256_300.txt";
    }
    ofstream ofs0(test);
    for(int i = 0; i < testImage.size(); i++)
    {
        ofs0 << testImage[i] << flush;
    }
    ofs0.close();
    ofstream ofs1(train_100);
    for(int i = 0; i < trainImage0.size(); i++)
    {
        ofs1 << trainImage0[i] << flush;
    }
    ofs1.close();
    ofstream ofs2(train_300);
    for(int i = 0; i < trainImage1.size(); i++)
    {
        ofs2 << trainImage1[i] << flush;
    }
    ofs2.close();

    return 0;
}