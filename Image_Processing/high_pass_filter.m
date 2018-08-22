% Image Sharpening using High Pass filter
clc;
clear all;

img = imread('images/cameraman.jpg');

m3 = -1 * ones(3) / 9;
m3(2,2) = 8/9;
m5 = -1 * ones(5) / 25;
m5(3,3) = 24/25;

figure(1);
subplot(2,2,[1 2]);
imshow(img);
title('Original Image');

sh3 = uint8(conv2(double(img), m3));
subplot(2,2,3);
imshow(sh3);
title('Filter with 3x3 mask');

sh5 = uint8(conv2(double(img), m5));
subplot(2,2,4);
imshow(sh5);
title('Filter with 5x5 mask');
