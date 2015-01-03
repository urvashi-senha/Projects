clc;clear;close all;
[input, map, alpha] = imread('eagle.jpg');
input = im2bw(input);
input=imcomplement(input);
original=input;
figure,subplot(3,1,1),imshow(input);
title('Input');
s = 3;

% Structuring element as square

[m, n] = size(input);
se_sqr = strel('square',s);


%% Iterative Erosion Method

n_skeletons = 30;
skeleton = zeros(n_skeletons,m,n);

for i=1:n_skeletons
    eroded_image = imerode(input,se_sqr);
    op_eroded_image = imerode(eroded_image,se_sqr);
    op_dilated_image = imdilate(op_eroded_image,se_sqr);
    skeleton(i,:,:) = eroded_image-op_dilated_image;
    input = eroded_image;
end

output = zeros(m, n);
for k=1:n_skeletons
    for i=1:m
        for j=1:n
            output(i,j) = output(i,j)|skeleton(k,i,j);
        end
    end
end
subplot(3,1,2),imshow(output);
title('Skeletonisation via iterative erosion');


%% Distance Transform Method

input = padarray(imcomplement(original), [5 5], 1);
output = input;
dist_matrix = bwdist(input,'quasi-euclidean');
b_size = 3;
for i=b_size+1:m-(b_size+1)
    for j=b_size+1:n-(b_size+1)
%         if dist_matrix(i,j) < max(max(dist_matrix(i-b_size:i+b_size,j-b_size:j+b_size)))-2
          if dist_matrix(i,j) < max(max(dist_matrix(i-b_size:i+b_size,j-b_size:j+b_size)))-2
            output(i,j) = 1;
        end
    end
end
subplot(3,1,3),imshow(imcomplement(output));
title('Skeletonisation via Cityblock Distance Measure');