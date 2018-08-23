% DCT for a 2D image
clc;
clear all;

a = imread('images/cameraman.jpg');
a = im2double(a);
figure(1);

subplot(2,2,1);
imshow(a);
title('Original Image');

b = dct2(a);
m = abs(b);
subplot(2,2,2);
plot(m);
title('Histogram');
xlabel('Frequency Bin');
ylabel('Amplitude');

subplot(2,2,3);
imshow(b);
title('DCT');

x = idct2(b);
subplot(2,2,4);
imshow(x);
title('Recovered Image');
