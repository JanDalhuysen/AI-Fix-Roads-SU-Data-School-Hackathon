#pragma once
#include <cstdarg>
namespace Eloquent {
    namespace ML {
        namespace Port {
            class LinearRegression {
                public:
                    /**
                    * Predict class for features vector
                    */
                    float predict(float *x) {
                        return dot(x, 0.000000032089) + 0.8042301210951552;
                    }

                protected:
                    /**
                    * Compute dot product
                    */
                    float dot(float *x, ...) {
                        va_list w;
                        va_start(w, 1);
                        float dot = 0.0;

                        for (uint16_t i = 0; i < 1; i++) {
                            const float wi = va_arg(w, double);
                            dot += x[i] * wi;
                        }

                        return dot;
                    }
                };
            }
        }
    }