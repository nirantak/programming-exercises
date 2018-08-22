% Image Smoothing using Average filter
clc;
clear all;

img = imread('images/cameraman.jpg');

var = [0.12,0.15];
f3 = ones(3) / 9;
f5 = ones(5) / 25;
l = length(var);
c = 0;
figure(1);

for t = 1:1:l
  noisy_img = imnoise(img, 'gaussian', var(t));

  subplot(2,3,t+c);
  imshow(noisy_img);
  title(['Gaussian Noise variance: ', num2str(var(t))]);

  fil3 = uint8(filter2(f3, double(noisy_img)));
  fil5 = uint8(filter2(f5, double(noisy_img)));

  subplot(2,3,t+1+c);
  imshow(fil3);
  title('Filter with 3x3 mask');

  subplot(2,3,t+2+c);
  imshow(fil5);
  title('Filter with 5x5 mask');
  c = c+2;
end
