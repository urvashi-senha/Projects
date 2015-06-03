package com.example.health_connect;



import java.io.File;

import com.parse.ParseFile;
import com.parse.ParseObject;
import com.parse.ParseUser;

import android.app.Activity;
import android.content.Intent;
import android.os.Bundle;
import android.support.v4.app.Fragment;
import android.view.LayoutInflater;
import android.view.View;
import android.view.View.OnClickListener;
import android.view.ViewGroup;
import android.widget.Button;
import android.widget.EditText;
import android.widget.TextView;
import android.widget.Toast;

public class MySampleFragment2 extends Fragment implements OnClickListener {
	
	
	
	
	private static final int REQUEST_PICK_FILE = 1;



	private static final int RESULT_OK = -1;

	

    public TextView mFilePathTextView;
    public Button mStartActivityButton;
    public File selectedFile;
	public static View mView;

    public static final MySampleFragment2 newInstance(String sampleText) {
        MySampleFragment2 f = new MySampleFragment2();

        Bundle b = new Bundle();
        f.setArguments(b);

    return f;
    }

    @Override
    public View onCreateView(LayoutInflater inflater, ViewGroup container, Bundle savedInstanceState) {

        mView = inflater.inflate(R.layout.sample_fragment2, container, false);
        mFilePathTextView = (TextView)mView.findViewById(R.id.textView4);
	    mStartActivityButton = (Button)mView.findViewById(R.id.button1);
	    mStartActivityButton.setOnClickListener(this);

        return mView;
    }
    
    public void onClick(View v) {
		switch(v.getId()) {
        case R.id.button1:
            // Create a new Intent for the file picker activity
            Intent intent = new Intent(mView.getContext(), FilePickerActivity.class);

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
            }

    	}
    
    
    
    public void onActivityResult(int requestCode, int resultCode, Intent data) {
	       if(resultCode==RESULT_OK) {
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
	            			Intent intent = new Intent(mView.getContext(), MainActivity.class);
	            			startActivity(intent);
	            		}
	                    
	                    Button bt = (Button) mView.findViewById(R.id.button2);
	                    bt.setOnClickListener(new OnClickListener() {
							
							@Override
							public void onClick(View v) {
								// TODO Auto-generated method stub
								
								
								byte[] dat = "Working at Parse is great!".getBytes();
			                    ParseFile fil = new ParseFile(mFilePathTextView.getText().toString(), dat);
			                    fil.saveInBackground();
			                    EditText sub = (EditText) mView.findViewById(R.id.sub);
			                    EditText rep = (EditText) mView.findViewById(R.id.head);
			              //      currentUser.put("Subject",sub.getText().toString());
			                //    currentUser.put("ReportHeading",rep.getText().toString());
			            		
			                    ParseObject f = new ParseObject("FILES");
			                    f.put("file", fil);
			                    f.put("Subject",sub.getText().toString());
			                    f.put("ReportHeading",rep.getText().toString());
			                    f.put("U_id", currentUser.getObjectId());
			             //       currentUser.put("FILE_h",fil);
			                    
			            
			                    
			                    f.saveInBackground();
								mFilePathTextView.setText("Done !!");
								MessageBox("File Successfully Uploaded");
								Intent intent = new Intent(mView.getContext(), SwipeHome.class);
		            			startActivity(intent);
								
							}
						});
	                    
	                    
	                    
	              
	                }
	            }
	        }
	    }
    public void MessageBox(String message)
    {
       Toast.makeText(mView.getContext(), message, Toast.LENGTH_SHORT).show();
    } 
}