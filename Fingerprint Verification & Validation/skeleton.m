function [ newim ] = skeleton( im, margin )
%UNTITLED2 Summary of this function goes here
%   Detailed explanation goes here

% input = padarray(imcomplement(original), [250 250], 1);
% [m, n] = size(input);
% output = input;
% dist_matrix = bwdist(input,'cityblock');
% b_size = 1;
% for i=b_size+1:m-(b_size+1)
%     for j=b_size+1:n-(b_size+1)
%           if dist_matrix(i,j) < max(max(dist_matrix(i-b_size:i+b_size,j-b_size:j+b_size)))-2
%             output(i,j) = 1;
%         end
%     end
% end


 % With n = Inf, thins objects to lines. It removes pixels so that an object
        % without holes shrinks to a minimally connected stroke, and an object with
        % holes shrinks to a connected ring halfway between each hole and the outer
        % boundary. This option preserves the Euler number.
        im = bwmorph(im,'thin',Inf);
       
       
        % now clean up the thin image
        im = bwmorph(im,'clean');       % Removes single isolated pixels        
        im = bwmorph(im,'hbreak');              % Removes H-Breaks      
        newim = bwmorph(im,'spur');     % Removes spikes
       
    % Remove the connected regions at the boundary.
    if nargin == 2
        [w,h] = size(newim);
        newim(1:margin-1,:)=0;
        newim(:,1:margin-1)=0;
        newim(:,h-margin+2:h)=0;
        newim(w-margin+2:w,:)=0;
    end;

end

