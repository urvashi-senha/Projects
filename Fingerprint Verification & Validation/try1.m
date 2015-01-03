clc;
clear;
close all;

%% converting to bw

img = imread('/home/arwa/Desktop/smai/Project/Dataset/DB1_B/103_4.tif');
yo = mean(mean(img))/256;
img1 = im2bw(img,yo);

%% getting the details

h = fspecial('laplacian');
img2 = imfilter(img,h);

%% thinning the image

BW3 = bwmorph(img2,'thin',Inf);

%% plotting the image

subplot(1,2,1);
imshow(img1);
subplot(1,2,2);
imshow(BW3);
