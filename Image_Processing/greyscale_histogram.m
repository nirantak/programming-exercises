% Equalize histogram for greyscale image
clc;
img = imread('images/binary_bw.jpg');
img = im2bw(img);
maxValue = max(img(:));
fprintf('\nSize: %d x %d x %d', size(img));
fprintf('\nUnique values: %d\n', length(unique(img)));
fprintf('\nMax value: %d\n', maxValue);

figure(1);
subplot(2,2,1);
imshow(img);
title('Original Image');

subplot(2,2,2);
imhist(img);
title('Histogram');

eq = histeq(img);
subplot(2,2,3);
imshow(eq);
title('Equalized Image');

subplot(2,2,4);
imhist(eq);
title('Equalized Histogram');
