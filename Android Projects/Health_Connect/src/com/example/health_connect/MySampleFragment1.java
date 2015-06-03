package com.example.health_connect;



import com.parse.Parse;
import com.parse.ParseUser;

import android.content.Intent;
import android.os.Bundle;
import android.support.v4.app.Fragment;
import android.view.LayoutInflater;
import android.view.Menu;
import android.view.View;
import android.view.ViewGroup;
import android.view.View.OnClickListener;
import android.widget.Button;
import android.widget.EditText;
import android.widget.TextView;
import android.widget.Toast;

public class MySampleFragment1 extends Fragment {
	
	
	
	
	private static View mView;

    public static final MySampleFragment1 newInstance(String sampleText) {
        MySampleFragment1 f = new MySampleFragment1();

        Bundle b = new Bundle();
        f.setArguments(b);

    return f;
    }

    @Override
    public View onCreateView(LayoutInflater inflater, ViewGroup container, Bundle savedInstanceState) {

        mView = inflater.inflate(R.layout.sample_fragment1, container, false);
        Parse.initialize(mView.getContext(), "e0FVFRBMAWJi5shg4XF8zL3SIuRwDIufww3338so", "toTJmlHTEF43u7PoAFT4fedwqfhoWiSajj1Se7FT");
        final ParseUser currentUser = ParseUser.getCurrentUser();
//		EditText e_name = (EditText) findViewById(R.id.editText1);
//		EditText e_eid = (EditText) findViewById(R.id.editText2);
		final EditText e_nat = (EditText) mView.findViewById(R.id.editText3);
		final EditText e_dob = (EditText) mView.findViewById(R.id.editText4);
		final EditText e_w = (EditText) mView.findViewById(R.id.editText5);
		final EditText e_h = (EditText) mView.findViewById(R.id.editText6);
		final EditText e_bg = (EditText) mView.findViewById(R.id.editText7);
		final EditText e_fname = (EditText) mView.findViewById(R.id.editText8);
		final EditText e_da = (EditText) mView.findViewById(R.id.editText9);
		
	//	e_name.setText(currentUser.getUsername());
		e_bg.setText(currentUser.getString("BG"));
		e_dob.setText(currentUser.getString("Dob"));
		e_fname.setText(currentUser.getString("Fname"));
		e_h.setText(currentUser.getString("Height"));
		e_nat.setText(currentUser.getString("Nation"));
		e_w.setText(currentUser.getString("Weight"));
	//	e_eid.setText(currentUser.getEmail());
		e_da.setText(currentUser.getString("DA"));
		TextView a_na = (TextView) mView.findViewById(R.id.na);
		TextView a_ei = (TextView) mView.findViewById(R.id.ei);
		
		
		a_na.setText(currentUser.getUsername());
		a_ei.setText(currentUser.getEmail());
		
		Button sz = (Button) mView.findViewById(R.id.save);
		sz.setOnClickListener(new OnClickListener() {
			
			@Override
			public void onClick(View v) {
				// TODO Auto-generated method stub
				currentUser.put("BG", e_bg.getText().toString());
				currentUser.put("Dob", e_dob.getText().toString());
				currentUser.put("Fname", e_fname.getText().toString());
				currentUser.put("Height", e_h.getText().toString());
				currentUser.put("Nation", e_nat.getText().toString());
				currentUser.put("Weight", e_w.getText().toString());
				currentUser.put("DA", e_da.getText().toString());
				currentUser.saveInBackground();
				MessageBox("Changes Saved");
				Intent i2= new Intent(mView.getContext(),SwipeHome.class);
				startActivity(i2);
			}
		});
		

        return mView;
    }

    public void MessageBox(String message)
    {
       Toast.makeText(mView.getContext(), message, Toast.LENGTH_SHORT).show();
    }  
	

}

