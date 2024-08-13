#include <iostream>
#include <string>
#include <cmath>
#include "learn_linear_to_c_1.h"

using namespace std;

int main(int argc, char *argv[])
{
    string input_value = argv[1];
    float input[1] = {stof(input_value)};
    // float input[1] = {argv[1]};

    Eloquent::ML::Port::LinearRegression model;

    int a = model.predict(input);
    float b = model.predict(input);
    double c = model.predict(input);

    std::cout << a << std::endl;
    std::cout << b << std::endl;
    std::cout << c << std::endl;

    std::cout << (floor((c * 2) + 0.5) / 2);
}
