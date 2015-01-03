package com.example.health_connect;

import java.io.ByteArrayOutputStream;
import java.io.File;
import java.io.FileNotFoundException;
import java.io.IOException;
import java.io.InputStream;


import android.net.Uri;
import android.os.Bundle;
import android.app.Activity;
import android.content.Intent;
import android.graphics.Bitmap;
import android.graphics.BitmapFactory;
import android.util.Log;
import android.view.Menu;
import android.view.View;
import android.view.View.OnClickListener;
import android.widget.Button;
import android.widget.ImageView;
import android.widget.TextView;
import com.parse.Parse;
import com.parse.ParseAnalytics;
import com.parse.ParseFile;
import com.parse.ParseUser;

public class Fourth extends Activity implements OnClickListener {

    private static final int REQUEST_PICK_FILE = 1;

    private TextView mFilePathTextView;
    private Button mStartActivityButton;
    private File selectedFile;

    @Override
    public void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.fourth);
        Parse.initialize(this, "e0FVFRBMAWJi5shg4XF8zL3SIuRwDIufww3338so", "toTJmlHTEF43u7PoAFT4fedwqfhoWiSajj1Se7FT");
		ParseAnalytics.trackAppOpened(getIntent());
		final ParseUser currentUser = ParseUser.getCurrentUser();
		if (currentUser == null)
		{
			Intent intent = new Intent(Fourth.this, MainActivity.class);
			startActivity(intent);
		}
		Button sk = (Button) findViewById(R.id.button2);
		sk.setOnClickListener(new OnClickListener() {
			
			@Override
			public void onClick(View v) {
				// TODO Auto-generated method stub
				Intent intent = new Intent(Fourth.this, SwipeHome.class);
    			startActivity(intent);
				
			}
		});
        // Set the views
        mFilePathTextView = (TextView)findViewById(R.id.file_path_text_view);
        mStartActivityButton = (Button)findViewById(R.id.start_file_picker_button);
        mStartActivityButton.setOnClickListener(this);      
    }

    public void onClick(View v) {
        switch(v.getId()) {
        case R.id.start_file_picker_button:
            // Create a new Intent for the file picker activity
            Intent intent = new Intent(this, FilePickerActivity.class);

            // Set the initial directory to be the sdcard
            //intent.putExtra(FilePickerActivity.EXTRA_FILE_PATH, Environment.getExternalStorageDirectory());

            // Show hidden files
            //intent.putExtra(FilePickerActivity.EXTRA_SHOW_HIDDEN_FILES, true);

            // Only make .png files visible
            //ArrayList<String> extensions = new ArrayList<String>();
            //extensions.add(".png");
            //intent.putExtra(FilePickerActivity.EXTRA_ACCEPTED_FILE_EXTENSIONS, extensions);

            // Start the activity
            startActivityForResult(intent, REQUEST_PICK_FILE);
            break;

        //case R.id.You_can_handle_more_onclick_events_from_here:
            //Do something
        //    break;
        }
    }

    @Override
    protected void onActivityResult(int requestCode, int resultCode, final Intent data) {
        if(resultCode == RESULT_OK) {
            switch(requestCode) {
            case REQUEST_PICK_FILE:
                if(data.hasExtra(FilePickerActivity.EXTRA_FILE_PATH)) {
                    // Get the file path
                    selectedFile = new File(data.getStringExtra(FilePickerActivity.EXTRA_FILE_PATH));
                    // Set the file path text view
                    mFilePathTextView.setText(selectedFile.getPath());  
                    //Now you have your selected file, You can do your additional requirement with file.  
                    final ParseUser currentUser = ParseUser.getCurrentUser();
                    if (currentUser == null)
            		{
            			Intent intent = new Intent(Fourth.this, MainActivity.class);
            			startActivity(intent);
            		}
                    
                    
                    
                    Button sk = (Button) findViewById(R.id.button2);
            		sk.setOnClickListener(new OnClickListener() {
            			
            			@Override
            			public void onClick(View v) {
            				// TODO Auto-generated method stub
            				Intent intent = new Intent(Fourth.this, SwipeHome.class);
                			startActivity(intent);
            				
            			}
            		});
                    
                     		
            		
            		
            		Log.d("Check","no prob till here");
                    
                    
                    Button bt = (Button) findViewById(R.id.button1);
       
                    bt.setOnClickListener(new OnClickListener() {
						
						@Override
						public void onClick(View v) {
							// TODO Auto-generated method stub
							
							
							
							Bitmap bitmap = null;
							byte[] imageInByte = null;
							
							
							  try {						        
						            InputStream stream = getContentResolver().openInputStream(Uri.fromFile(selectedFile));

						            bitmap = BitmapFactory.decodeStream(stream);
						            stream.close();
						           Log.d("Check","REACHED!");
						      //      ImageView image = (ImageView) findViewById(R.id.imageView1);
						      //      image.setImageBitmap(bitmap);
						            //picNameText.setText("Selected: en"
						                //  + getStringNameFromRealPath(fileName));

						            ByteArrayOutputStream stream1 = new ByteArrayOutputStream();
						            bitmap.compress(Bitmap.CompressFormat.PNG, 100, stream1);
						            imageInByte = stream1.toByteArray();

						        }catch (FileNotFoundException e) {
						            e.printStackTrace();
						        }
						        catch (IOException e) {
						            e.printStackTrace();
						        } 
							
							  
							
					
							
							byte[] dat = "Working at Parse is great!".getBytes();
		                    ParseFile fil = new ParseFile(mFilePathTextView.getText().toString(), imageInByte);
		                    fil.saveInBackground();
		                   
		            		Log.d("Check",imageInByte.length+" end");
		                    currentUser.put("FILE",fil);
		                    currentUser.saveInBackground();
							mFilePathTextView.setText("Done !!");
							Intent intent = new Intent(Fourth.this, SwipeHome.class);
	            			startActivity(intent);
							
						}
					});
                    
                    
                    
                 //mFilePathTextView.setText("Done");
                }
            }
        }
    }
}