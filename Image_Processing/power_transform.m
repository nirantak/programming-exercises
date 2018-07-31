% Power transformation
clc;
a = imread('images/gray1.jpg');
[m,n] = size(a);
maxValue = max(a(:));
fprintf('\nSize: %d x %d x %d', size(a));
fprintf('\nUnique values: %d\n', length(unique(a)));
fprintf('\nMax value: %d\n', maxValue);

figure(1);
subplot(2,2,1);
imshow(a);
title('Original Image');

subplot(2,2,2);
imhist(a);
title('Original Histogram');

gamma = 1.1;
d = double(a).^gamma;

subplot(2,2,3);
imshow(uint8(d));
title('Power Transformed Image');

subplot(2,2,4);
imhist(uint8(d));
title('Power Transformed Histogram');
