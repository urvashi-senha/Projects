clc;clear all;close all;

im1=double(imread('/home/arwa/Desktop/smai/Project/Dataset/DB1_B/103_1.tif'));
if ndims(im1)==3
    im1=rgb2gray(im1);
end
% figure,imshow(uint8(im1));
% title('Input Image');
im=im1;
ma=mean(im1(:));
va=var(double(im1(:)));
[m,n]=size(im1);

%% Normalisation

% Let Md be  desired mean and Vd be desired var
Md=128;
Vd=10*va;
im=zeros(m,n,'double');
for i=1:m
    for j=1:n
        if im1(i,j)>ma
            im(i,j)=Md+sqrt(Vd*(im1(i,j)-ma)^2/va);
        else
            im(i,j)=Md-sqrt(Vd*(im1(i,j)-ma)^2/va);
        end
    end
end
% figure,imshow(uint8(im));
% title('Normalised Image');

%% Regional Masking

[w, h] = size(im);
for i=1:w-1
    for j=1:h-1 
        mask = double(im(i:i+6,j:j+6));
        v=var(mask(:));
        if v<250
            for l=i:i+6
                for m=j:j+6
                    im(l,m)=255;
                end
            end
        end
        if j<h-7
            j=j+7;
        else
            break;
        end
    end
    if i<w-7
        i = i+7;
    else
        break;
    end
end
% figure,imshow(uint8(im));
% title('After foreground extraction using regional masking');


%% Creation of Gabor Wavelets Filter

ga = gaborFilterBank(4,16,15,15);
F=zeros([4,16,m,n]);
fin=zeros(m,n,2);
ma=NaN*zeros(m,n);
for i=1:4
    for j=1:16
        F=conv2(im,ga{i,j});
        for k=1:m
            for l=1:n
                if ma(k,l)<abs(F(k,l))
                    ma(k,l)=abs(F(k,l));
                    fin(k,l,1)=((2*i)-1)/25;
                    fin(k,l,2)=(j-1)*pi/16;
                end
            end
        end
    end
end

%% Gaussian Filtering of the Gabor wavelet features

finc=cos(2*fin(:,:,2));
fins=sin(2*fin(:,:,1));
myfilter = fspecial('gaussian',[3 3], 1);
finc=imfilter(finc,myfilter);
fins=imfilter(fins,myfilter);
fin(:,:,2)=atan2(fins,finc);

myfilter = fspecial('gaussian',[3 3], 1);
fin(:,:,1)=imfilter(fin(:,:,1),myfilter);


%% Gabor Filtering

i=0;
x=-1:1;
y=-1:1;
gau=zeros(3,3);
ff=fft2(im);
while(1)
    j=0;
    if 3+3*i>=size(ff,1) && 3+3*i>=n
            break;
    end
    while(1)
        if 3+3*j>=size(ff,2) && 3+3*j>=m
            break;
        end
        u=x*cos(fin(2+3*i,2+3*j,2))+y*sin(fin(2+3*i,2+3*j,2));
        v=-1*x*sin(fin(2+3*i,2+3*j,2))+y*cos(fin(2+3*i,2+3*j,2));
        for k=1:3
            for l=1:3
                gau(k,l)=exp(-.5*(u(k)^2+v(l)^2)/0.005)*cos(2*pi*u(k)*sqrt(2)^(fin(2+3*i,2+3*j,1)-1)/.25);
            end
        end
        ff(1+3*i:3*(1+i),1+3*j:3*(1+j))=filter2(gau,ff(1+3*i:3*(1+i),1+3*j:3*(1+j)));
        j=j+1;
    end
    i=1+i;
end
iff=real(ifft2(ff));
iff2=255*iff/max(iff(:));
iff3=filter2([1 1 1 1 1;1 1 1 1 1;1 1 1 1 1;1 1 1 1 1;1 1 1 1 1]/25,iff);
iff3=255*iff3/max(iff(:));
% figure()
% imshow(iff3)

%% Thresholding

iff3=im-iff3;
iff3(iff3>0)=255;
iff3(iff3<=0)=0;
figure,imshow(uint8(iff3));


%% Binarisation

im3=im2bw(uint8(im),30/256);
figure,imshow(im3);
title('After Binarization');