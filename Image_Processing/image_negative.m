% Create negative of an image
clc;
img = imread('images/circles.png');
img = im2bw(img);
[m,n] = size(img);
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

%neg = maxValue - img;
neg = imcomplement(img);
subplot(2,2,3);
imshow(neg);
title('Negative Image');

subplot(2,2,4);
imhist(neg);
title('Negative Histogram');
