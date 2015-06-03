package com.example.health_connect;



import java.text.SimpleDateFormat;
import java.util.Calendar;
import java.util.Random;

import com.parse.Parse;
import com.parse.ParseAnalytics;
import com.parse.ParseUser;

import android.content.Intent;
import android.os.Bundle;
import android.support.v4.app.Fragment;
import android.util.Log;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.ImageView;
import android.widget.TextView;

public class MySampleFragment extends Fragment {
	 private static View mView;
	 
	 

	    public static final MySampleFragment newInstance(String sampleText) {
	        MySampleFragment f = new MySampleFragment();
	        
	        Bundle b = new Bundle();
	        f.setArguments(b);

	    return f;
	    }

	    @Override
	    public View onCreateView(LayoutInflater inflater, ViewGroup container, Bundle savedInstanceState) {

	        mView = inflater.inflate(R.layout.sample_fragment, container, false);
	        Parse.initialize(mView.getContext(), "e0FVFRBMAWJi5shg4XF8zL3SIuRwDIufww3338so", "toTJmlHTEF43u7PoAFT4fedwqfhoWiSajj1Se7FT");
	        
	      
			
			ParseUser currentUser = ParseUser.getCurrentUser();
			Log.d("Check",currentUser.getObjectId());
	        ImageView birthdaypic = (ImageView) mView.findViewById(R.id.imageView2);
			TextView wish = (TextView) mView.findViewById(R.id.textView23);
			TextView hbday = (TextView) mView.findViewById(R.id.textView24);
			
			String date_of_birth = currentUser.getString("Dob");
			
			Calendar c = Calendar.getInstance();
			SimpleDateFormat df = new SimpleDateFormat("dd/MM/yyyy");
			String formattedDate = df.format(c.getTime());
			//Log.d("Check",formattedDate);
			String str[]={ "Every patient carries her or his own doctor inside." , 
					"Laughter is the best medicine",
					"The art of medicine consists in amusing the patient while nature cures the disease.",
					"Health is wealth",
					"My health is good,it's my age that's bad.",
					"A healthy body is a guest-chamber for the soul; a sick body is a prison.",
					"Fitness:If it came in a bottle,everybody would have a good body.",
					"Ypu don't get ulcers form what you eat,but from what's eating you.",
					"Those who don't find time for exercise will have to find time for illness.",
					"Sickness comes on horseback and departs on foot.",
					"Health and appetite impart the sweetness to sugar,bread and meat.",
					"Health is not valued till sickness comes.",
					"Health is not simply the absence of sickness.",
					"To eat is a necessity,but to eat intelligently is an art.",
					"Let food be the medicine,thy medicine shall be thy food.",
					"Food is fuel,choose wisely.",
					"Health and intellect are the two blessings of life.",
					"The greatest wealth is health.",
					"Think positive and focus on gratitude.",
					"Get a good night's sleep.",
					"Use food over supplements.",
					"Eat 5 servings of fruits and veggies a day.",
					"Big idea: Be happy :)",
					"Drink water instead of surgery drinks.",
					"Swap big serves for smaller ones.",
					"Park the car and walk the rest of the way.",
					"No disease that can be treated by diet should be treated with any other means.",
					"Your body hears everything your mind says/",
					"Take care of your body. It's the only place you have to live.",
					"Every human being is the author of his own health or disease."
			};
			Random r = new Random();
			int High =30;  // 30 excluded
			int Low=0;
			int random_number = r.nextInt(High-Low) + Low;
			
			if( (formattedDate.substring(0,2).equalsIgnoreCase(date_of_birth.substring(0,2))) && (formattedDate.substring(3,5).equalsIgnoreCase( date_of_birth.substring(3,5))) )
		//	if(d1==d2 && m1==m2)
			{		
			
				
			}
			else
			{
			//	Log.d("Check", d1);
				birthdaypic.setImageDrawable(null);
				wish.setText(null);
				hbday.setText(null);
				wish.setText(str[random_number]);
				//wish.setVisibility(View.GONE);
				hbday.setVisibility(View.GONE);
			}
			
			
		
			TextView a_name = (TextView) mView.findViewById(R.id.textView6);
			TextView a_eid = (TextView) mView.findViewById(R.id.textView8);
			TextView a_nat = (TextView) mView.findViewById(R.id.textView10);
			TextView a_dob = (TextView) mView.findViewById(R.id.textView12);
			TextView a_w = (TextView) mView.findViewById(R.id.textView14);
			TextView a_h = (TextView) mView.findViewById(R.id.textView16);
			TextView a_bg = (TextView) mView.findViewById(R.id.textView18);
			TextView a_fname = (TextView) mView.findViewById(R.id.textView20);
			TextView a_da = (TextView) mView.findViewById(R.id.textView22);
			a_name.setText(currentUser.getUsername());
			a_bg.setText(currentUser.getString("BG"));
			a_dob.setText(currentUser.getString("Dob"));
			a_fname.setText(currentUser.getString("Fname"));
			a_h.setText(currentUser.getString("Height"));
			a_nat.setText(currentUser.getString("Nation"));
			a_w.setText(currentUser.getString("Weight"));
			a_eid.setText(currentUser.getEmail());
			a_da.setText(currentUser.getString("DA"));
			
	        

	        return mView;
	    }
	}
	
