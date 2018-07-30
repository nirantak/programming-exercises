% Image channel splitting

im_color = imread('images/color1.jpg');
imshow(im_color);
double(im_color);
[m,n] = size(im_color);
maxValue = max(im_color(:));
fprintf('\nSize: %d x %d x %d', size(im_color));
fprintf('\nUnique values: %d\n', length(unique(im_color)));
fprintf('\nMax value: %d\n', maxValue);

figure(1);
subplot(2,2,1);
imshow(im_color);
title('Original Image');

% A color image is represented with (R,G,B) channels

a_red = im_color; %Assign the intensity values to another matrix
a_red(:,:,2) = 0; %Make Channel=2 i.e. green component zero
a_red(:,:,3) = 0; %Make Channel=3 i.e. blue component zero
subplot(2,2,2);
imshow(a_red);
title('Red Channel');

a_green = im_color;
a_green(:,:,1) = 0; %Make Channel=1 i.e. red component zero
a_green(:,:,3) = 0; %Make Channel=3 i.e. blue component zero
subplot(2,2,3);
imshow(a_green);
title('Green Channel');

a_blue = im_color;
a_blue(:,:,1) = 0; %Make Channel=1 i.e. red component zero
a_blue(:,:,2) = 0; %Make Channel=2 i.e. green component zero
subplot(2,2,4);
imshow(a_blue);
title('Blue Channel');
