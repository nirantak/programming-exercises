% Grey level slicing without background
clc;
a = imread('images/gray1.jpg');
a = double(a);
b = double(a);
[m,n] = size(a);
maxValue = max(a(:));
fprintf('\nSize: %d x %d x %d', size(a));
fprintf('\nUnique values: %d\n', length(unique(a)));
fprintf('\nMax value: %d\n', maxValue);

figure(1);
subplot(2,2,1);
imshow(uint8(a));
title('Original Image');

subplot(2,2,2);
imhist(uint8(a));
title('Original Histogram');

for i = 1:1:m
	for j = 1:1:n
		if((b(i,j)>90)) && (b(i,j)<150)
			b(i,j) = 225;
		else
			b(i,j) = 0;
		end
	end
end

subplot(2,2,3);
imshow(uint8(b));
title('New Image');

subplot(2,2,4);
imhist(uint8(b));
title('New Histogram');
