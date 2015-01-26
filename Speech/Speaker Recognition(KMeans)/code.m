
dirData = dir('dataset/feats/train'); 
dirIndex = [dirData.isdir];
subDirs = {dirData(dirIndex).name};

index = subDirs(3:end);

 for i=3:length(subDirs)
    a = subDirs(i);
    a = a{:};
    b = strcat('dataset/feats/train/',a);
    getCentroid(b);
 end