% Zoom image
clc;
clear all;

img = imread('images/circles.png');
rows = size(img,1);
cols = size(img,2);
new_img = zeros(2*rows, 2*cols, size(img,3), class(img));

new_img(1:2:end,1:2:end,:) = img; %// Left
new_img(2:2:end,1:2:end,:) = img; %// Bottom
new_img(1:2:end,2:2:end,:) = img; %// Right
new_img(2:2:end,2:2:end,:) = img; %// Bottom-Right

new_img = imcrop(new_img, [0,0,cols,rows]);

figure(1);
subplot(2,2,1);
imshow(img);
title('Image');

subplot(2,2,2);
imhist(img);
title('Histogram');

subplot(2,2,3);
imshow(new_img);
title('Zoom');

subplot(2,2,4);
imhist(new_img);
title('Histogram');
