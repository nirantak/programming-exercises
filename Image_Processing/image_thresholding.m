% Image thresholding
clc;
img = imread('images/gray1.jpg');
%img = im2bw(img);
[m,n] = size(img);
maxValue = max(img(:));
fprintf('\nSize: %d x %d x %d', size(img));
fprintf('\nUnique values: %d\n', length(unique(img)));
fprintf('\nMax value: %d\n', maxValue);

thresh = [50, 100, 150];
lt = length(thresh);

figure(1);
subplot(2,lt+1,1);
imshow(img);
title('Original Image');

subplot(2,lt+1,1+lt);
imhist(img);
title('Original Histogram');

for t = 1:1:lt
	for i = 1:1:m
		for j = 1:1:n
			if(img(i,j) < thresh(t))
				new_img(i,j) = 0;
			else
				new_img(i,j) = 255;
			end
		end
	end

	subplot(2,lt+1,1+t);
	imshow(new_img);
	title(['Threshhold ', num2str(thresh(t))]);

	subplot(2,lt+1,lt+1+t);
	imhist(new_img);
	title(['Histogram ', num2str(thresh(t))]);
end
