% Contrast Stretching a grayscale image
clc;
a = imread('images/gray1.jpg');
%img = im2bw(img);
[m,n] = size(a);
maxValue = max(a(:));
fprintf('\nSize: %d x %d x %d', size(a));
fprintf('\nUnique values: %d\n', length(unique(a)));
fprintf('\nMax value: %d\n', maxValue);

lt = 100;
ut = 200;

figure(1);
subplot(2,2,1);
imshow(a);
title('Original Image');

subplot(2,2,2);
imhist(a);
title('Original Histogram');

for x1:1:m
	for y = 1:1:n
		if a(x,y) <= lt
			b(x,y) = 0.5 * a(x,y);
		else if a(x,y) <= ut
			b(x,y) = 2*(a(x,y) - lt) + 0.5*ut;
		else
			b(x,y) = 0.5*(a(x,y)-ut) + 0.5*lt + 2*(ut-lt);
		end
	end
end

subplot(2,2,3);
imshow(b);
title('New Image');

subplot(2,2,4);
imhist(b);
title('New Histogram');
