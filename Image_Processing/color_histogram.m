% Equalize histogram for a color image
clc;
img = imread('images/binary_color.jpg');
maxValue = max(img(:));
fprintf('\nSize: %d x %d x %d', size(img));
fprintf('\nUnique values: %d\n', length(unique(img)));
fprintf('\nMax value: %d\n', maxValue);

figure(2);
% Red Channel
a_red = img(:,:,1);
subplot(3,4,1);
imshow(a_red);
title('Red Channel');

subplot(3,4,2);
imhist(a_red);
title('Red Histogram');

eq_r = histeq(a_red);
subplot(3,4,3);
imhist(eq_r);
title('Red Equalized Histogram');

subplot(3,4,4);
imshow(eq_r);
title('Red Equalized Image');

% Green Channel
a_green = img(:,:,2);
subplot(3,4,5);
imshow(a_green);
title('Green Channel');

subplot(3,4,6);
imhist(a_green);
title('Green Histogram');

eq_g = histeq(a_green);
subplot(3,4,7);
imhist(eq_g);
title('Green Equalized Histogram');

subplot(3,4,8);
imshow(eq_g);
title('Green Equalized Image');

% Blue Channel
a_blue = img(:,:,3);
subplot(3,4,9);
imshow(a_blue);
title('Blue Channel');

subplot(3,4,10);
imhist(a_blue);
title('Blue Histogram');

eq_b = histeq(a_blue);
subplot(3,4,11);
imhist(eq_b);
title('Blue Equalized Histogram');

subplot(3,4,12);
imshow(eq_b);
title('Blue Equalized Image');

% Combined images
figure(1);
subplot(2,2,1);
imshow(img);
title('Original Image');

subplot(2,2,3);
imhist(img);
title('Original Histogram');

img_eq = cat(3, eq_r, eq_g, eq_b);
subplot(2,2,2);
imshow(img_eq);
title('Equalized Image');

subplot(2,2,4);
imhist(img_eq);
title('Equalized Histogram');
