clc;
clear;

im = imread('Dataset/DB1_B/104_4.tif');
imshow(im,[]);

%% Identify ridge-like regions and normalise image
    blksze = 16; thresh = 0.1;
    [normim, mask] = ridgesegment(im, blksze, thresh);
    imshow(normim,[]);

%% Determine ridge orientations
    [orientim, reliability] = ridgeorient(normim, 1, 5, 5);
    plotridgeorient(orientim, 20, im, 2)
    figure();
    imshow(reliability,[])
    
%% Determine ridge frequency values across the image
    blksze = 36; 
    [freq, medfreq] = ridgefreq(normim, mask, orientim, blksze, 5, 5, 15);
    figure();
    imshow(freq,[]) 
    
    % Actually I find the median frequency value used across the whole
    % fingerprint gives a more satisfactory result...    
    freq = medfreq.*mask;
    
%% Now apply filters to enhance the ridge pattern
    newim = ridgefilter(normim, orientim, freq, 0.5, 0.5, 1);
    imshow(newim,[]);
    
    % Binarise, ridge/valley threshold is 0
    binim = newim > 0;
    imshow(binim,[]);
    
      
%% Skeletonize the image
    wo = skeleton((binim),5);
    wo = imcomplement(wo);
    figure();
    imshow(wo);
    thin_image = wo;

%% Minutiae extraction

    s=size(thin_image);
    N=3;%window size
    n=(N-1)/2;
    r=s(1)+2*n;
    c=s(2)+2*n;
    double temp(r,c);   
    temp=zeros(r,c);bifurcation=zeros(r,c);ridge=zeros(r,c);
    temp((n+1):(end-n),(n+1):(end-n))=thin_image(:,:);
    outImg=zeros(r,c,3);%For Display
    outImg(:,:,1) = temp .* 255;
    outImg(:,:,2) = temp .* 255;
    outImg(:,:,3) = temp .* 255;
    for x=(n+1+10):(s(1)+n-10)
        for y=(n+1+10):(s(2)+n-10)
            e=1;
            for k=x-n:x+n
                f=1;
                for l=y-n:y+n
                    mat(e,f)=temp(k,l);
                    f=f+1;
                end
                e=e+1;
            end;
            if(mat(2,2)==0)
                ridge(x,y)=sum(sum(~mat));
                bifurcation(x,y)=sum(sum(~mat));
            end
        end;
    end;

%% RIDGE END FINDING

    [ridge_x ridge_y]=find(ridge==2);
    len=length(ridge_x);
    %For Display
    for i=1:len
        outImg((ridge_x(i)-3):(ridge_x(i)+3),(ridge_y(i)-3),2:3)=0;
        outImg((ridge_x(i)-3):(ridge_x(i)+3),(ridge_y(i)+3),2:3)=0;
        outImg((ridge_x(i)-3),(ridge_y(i)-3):(ridge_y(i)+3),2:3)=0;
        outImg((ridge_x(i)+3),(ridge_y(i)-3):(ridge_y(i)+3),2:3)=0;
    
        outImg((ridge_x(i)-3):(ridge_x(i)+3),(ridge_y(i)-3),1)=255;
        outImg((ridge_x(i)-3):(ridge_x(i)+3),(ridge_y(i)+3),1)=255;
        outImg((ridge_x(i)-3),(ridge_y(i)-3):(ridge_y(i)+3),1)=255;
        outImg((ridge_x(i)+3),(ridge_y(i)-3):(ridge_y(i)+3),1)=255;
    end

%% BIFURCATION FINDING

    [bifurcation_x bifurcation_y]=find(bifurcation==4);
    temp_bifurcation = [bifurcation_x bifurcation_y];
    temp_bifurcation = unique(temp_bifurcation,'rows');
    len=length(bifurcation_x);
    %For Display
    for i=1:len
        outImg((bifurcation_x(i)-3):(bifurcation_x(i)+3),(bifurcation_y(i)-3),1:2)=0;
        outImg((bifurcation_x(i)-3):(bifurcation_x(i)+3),(bifurcation_y(i)+3),1:2)=0;
        outImg((bifurcation_x(i)-3),(bifurcation_y(i)-3):(bifurcation_y(i)+3),1:2)=0;
        outImg((bifurcation_x(i)+3),(bifurcation_y(i)-3):(bifurcation_y(i)+3),1:2)=0;
    
        outImg((bifurcation_x(i)-3):(bifurcation_x(i)+3),(bifurcation_y(i)-3),3)=255;
        outImg((bifurcation_x(i)-3):(bifurcation_x(i)+3),(bifurcation_y(i)+3),3)=255;
        outImg((bifurcation_x(i)-3),(bifurcation_y(i)-3):(bifurcation_y(i)+3),3)=255;
        outImg((bifurcation_x(i)+3),(bifurcation_y(i)-3):(bifurcation_y(i)+3),3)=255;
    end
figure;imshow(outImg);title('Minutiae');


%% Feature 

      