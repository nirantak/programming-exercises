% Point operations in spatial domain - Changing Image Brightness
clc;
img = imread('images/gray.png');

figure(1);
subplot(2,3,1);
imshow(img);
title('Original Image');

a = uint8(double(img) + 100);
subplot(2,3,2);
imshow(a);
title('Increased Brightness');

b = uint8(double(img) - 100);
subplot(2,3,3);
imshow(b);
title('Decreased Brightness');

subplot(2,3,4);
imhist(img);
title('Histogram - Original');

subplot(2,3,5);
imhist(a);
title('Histogram - Inc Brightness');

subplot(2,3,6);
imhist(b);
title('Histogram - Dec Brightness');
