#include <stdio.h>
#define PI 3.141592653589793

int main(int argc, const char *argv[])
{
	float r,h;
	printf("Input r and h : \n");
	scanf("%f %f",&r,&h);
	printf("圆周长:%.2f\n圆面积:%.2f\n圆球表面积:%.2f\n圆球体积:%.2f\n圆柱体积:%.2f\n",2*PI*r,PI*(r*r),4*PI*(r*r),4/(3*PI*(r*r*r)),PI*(r*r)*h);
	return 0;
}
