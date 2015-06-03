function getCentroid(fileName)
fileList = getAllFiles(fileName);
speaker = [];
c = [];

for i = 1 : length(fileList)
    a = fileList(i);
    a = a{:};
    A = dlmread(a,' ');
   % [p,q] = kmeans(A,1);
    %c = [c ; q];
   speaker = [ speaker; A ];
end

 [x1,y1] = kmeans(speaker,32);



%hold('on');
% for i = 1:length(speaker)
%     a = speaker(i,:);
%     if x(i) == 1;
%     plot(a(1,1),a(1,2),'r+');
%     else
%     plot(a(1,1),a(1,2),'g+');
%     end
% end
% a = y(1,:);
% % plot(a(1,1),a(1,2),'b*');
% a = y(2,:);
% % plot(a(1,1),a(1,2),'b*');

dlmwrite('Centroid_File',y1,'-append');

end

