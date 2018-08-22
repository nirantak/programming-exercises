% Image Smoothing using Median filter
clc;
clear all;

img = imread('images/cameraman.jpg');

var = [0.1,0.3];
l = length(var);
c = 0;
figure(1);

for t = 1:1:l
  noisy_img = imnoise(img, 'salt & pepper', var(t));

  subplot(2,3,t+c);
  imshow(noisy_img);
  title(['Salt & Pepper noise: ', num2str(var(t)*100), '%']);

  fil3 = uint8(medfilt2(double(noisy_img), [3 3]));
  fil5 = uint8(medfilt2(double(noisy_img), [5 5]));

  subplot(2,3,t+1+c);
  imshow(fil3);
  title('Filter with 3x3 mask');

  subplot(2,3,t+2+c);
  imshow(fil5);
  title('Filter with 5x5 mask');
  c = c+2;
end
