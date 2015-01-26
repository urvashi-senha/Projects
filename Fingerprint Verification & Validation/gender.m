clc;
clear;
close all;

% %% Calculating the fund freq from fft
% tot = 148;
% tempf = [];
% for i = 1:1:tot
%     if (i~=9 && i~=18 && i~=128) 
%         path = ['Female/' num2str(i) '.bmp'];
%         im =imread(path);
%         dim = fft2(im);
%         tempf = [tempf abs(dim(1))];
%     end
% end
% 
% save('female.mat','tempf');
% %save('female.mat','temp');

% %% Finding threshold
% load('female.mat');
% load('male.mat');
% 
% x = 1:1:145
% y = zeros(145)
% y(:) = 42000000
% figure();
% 
% plot(x,y,'-k');
% hold on;
% plot(x,temp,'-g');
% hold on;
% plot(x,tempf,'-r');
% title('Gender Detection')
% xlabel('Image No')
% ylabel('Fundamental Frequency')

% %% Classifying
% 
% thresh = 42000000;
% query = 'test/f52.bmp';
% im =imread(query);
% dim = fft2(im);
% 
% if dim< thresh
%     disp('female');
% else
%     disp('male');
% end

%% Finding Accuracy

count_m = 0;
thresh = 42000000;

load('male.mat');

for i=1:1:145
    if temp(i) > thresh
        count_m = count_m + 1;
    end
end

eff_m = (count_m*100)/145

count_f = 0;

load('female.mat');

for i=1:1:145
    if tempf(i) < thresh
        count_f = count_f + 1;
    end
end

eff_f = (count_f*100)/145
