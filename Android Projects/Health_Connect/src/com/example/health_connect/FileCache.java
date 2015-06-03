package com.example.health_connect;

import java.io.File;
import android.content.Context;
import android.util.Log;
 
public class FileCache {
 
    private File cacheDir;
 
    public FileCache(Context context) {
        // Find the dir to save cached images
        if (android.os.Environment.getExternalStorageState().equals(
                android.os.Environment.MEDIA_MOUNTED))
            {
        	cacheDir = new File(
            		
                    android.os.Environment.getExternalStorageDirectory(),
                     "health_connect");
        	Log.d("check15","in filecache class");
            }
        else{
        	Log.d("check16","in filecache class");
            cacheDir = context.getCacheDir();
            Log.d("check18","in filecache class");}
        if (!cacheDir.exists())
            {
        	Log.d("check17","in filecache class");
        	cacheDir.mkdirs();
            }
    }
 
    public File getFile(String url) {
        String filename = String.valueOf(url.hashCode());
        // String filename = URLEncoder.encode(url);
        File f = new File(cacheDir, filename);
        Log.d("check18","in filecache class");
        return f;
 
    }
 
    public void clear() {
        File[] files = cacheDir.listFiles();
        if (files == null)
            {
        	Log.d("check19","in filecache class");
        	return;
            }
        for (File f : files)
            f.delete();
    }
}