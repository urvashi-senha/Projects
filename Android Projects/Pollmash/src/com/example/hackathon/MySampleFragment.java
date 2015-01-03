package com.example.hackathon;

import java.util.ArrayList;
import java.util.List;

import com.parse.Parse;
import com.parse.ParseException;
import com.parse.ParseObject;
import com.parse.ParseQuery;
import com.parse.ParseUser;

import android.os.Bundle;
import android.app.Activity;
import android.content.Intent;
import android.support.v4.app.Fragment;
import android.text.Editable;
import android.text.TextWatcher;
import android.util.Log;
import android.view.KeyEvent;
import android.view.LayoutInflater;
import android.view.Menu;
import android.view.View;
import android.view.ViewGroup;
import android.view.View.OnClickListener;
import android.widget.AdapterView;
import android.widget.Button;
import android.widget.EditText;
import android.widget.ImageView;
import android.widget.ListView;
import android.widget.TextView;
import android.widget.ViewFlipper;
import android.widget.AdapterView.OnItemClickListener;

public class MySampleFragment extends Fragment implements TextWatcher,OnItemClickListener
{
	private static View mView;
	private static final int LIST_PIC_SCREEN = 0;
	private static final int VIEW_PIC_SCREEN = 1;
	List<ParseObject> pol;
	private ArrayList<String>listPicName = new ArrayList<String>();
	private ArrayList<String> listPicPosition = new ArrayList<String>();
	private ArrayList<String> listPicParty = new ArrayList<String>();
	private ArrayList<String> listPicState = new ArrayList<String>();
	private ArrayList<String> listPicConstituency = new ArrayList<String>();
	private ArrayList<Integer> listPicStockRate = new ArrayList<Integer>();
	private ArrayList<String> listPicId = new ArrayList<String>();
	private ArrayList<Patient> listPic = new ArrayList<Patient>();
	private ListView listview;
	private PatientPicAdapter adapter;
	private EditText searchEdt;
	private ViewFlipper fliper;

	private ImageView viewpic;
	private TextView viewname;
	private TextView viewstate;
	private TextView viewconstituency;
	private TextView viewposition;
	private TextView viewparty;

	public static final MySampleFragment newInstance(String sampleText) 
	{
		MySampleFragment f = new MySampleFragment();      
		Bundle b = new Bundle();
		f.setArguments(b);
		return f;
	}

	@Override
	public View onCreateView(LayoutInflater inflater, ViewGroup container, Bundle savedInstanceState) 
	{
		mView = inflater.inflate(R.layout.fragment, container, false);
		//  Parse.initialize(mView.getContext(), "e0FVFRBMAWJi5shg4XF8zL3SIuRwDIufww3338so", "toTJmlHTEF43u7PoAFT4fedwqfhoWiSajj1Se7FT");
		Parse.initialize(mView.getContext(), "Q41kE80rWOGz6khmLdhvMPSZd5CJL1YUw35ro9ht", "FaZ2FwBQj8fGCaPblg7T7o6qRX0HwHZNtqIydC68");
		ParseUser currentUser = ParseUser.getCurrentUser();
		Log.d("ERRRRROOORR!!!!","gh") ;
		if(currentUser != null)
		{
			Log.d("check!!!!", "before query");
			ParseQuery<ParseObject> query4 = new ParseQuery<ParseObject>("Politicians");
			//	query4.whereEqualTo("State",currentUser.get("Place"));
			Log.d("check!!!!", "before for");
			try
			{
				pol=query4.find(); 

				for(ParseObject r : pol)
				{
					listPicId.add((String)r.getObjectId());
					listPicName.add((String)r.get("Name"));
					Log.d("check!!!!", "add");
					listPicParty.add((String)r.get("Party"));
					listPicPosition.add((String)r.get("Position"));
					listPicState.add((String)r.get("State"));
					listPicConstituency.add((String)r.get("Constituency"));
					listPicStockRate.add((Integer)r.get("StockRate"));

				}
			}
			catch (ParseException e) 
			{
				// TODO Auto-generated catch block
				e.printStackTrace();
			}
		}

		fliper = (ViewFlipper)mView.findViewById(R.id.viewFlipper3);
		listview = (ListView)mView.findViewById(R.id.listView3);
		listPic.clear();

		for (int i = 0; i < listPicName.size(); i++) 
		{
			Log.d("Error","for loop");
			Patient pic = new Patient(listPicName.get(i),listPicParty.get(i),listPicState.get(i),listPicConstituency.get(i),
					listPicPosition.get(i),listPicStockRate.get(i),listPicId.get(i));
			Log.d("Error","pic added");
			listPic.add(pic);
		}
		adapter = new PatientPicAdapter(getActivity().getBaseContext(), listPic);
		Log.d("Error","returned from adapter");
		listview.setAdapter(adapter);
		Log.d("Error","in adapter");

		listview.setOnItemClickListener(new OnItemClickListener() 
		{
			public void onItemClick(AdapterView<?> parent, View view, final int position,  long id) 
			{
				Sliding.slideFromRightToLeft(VIEW_PIC_SCREEN, fliper);
				//	viewpic.setImageResource(listPic.get(position).getPicSource());
				viewname.setText(listPic.get(position).getPicName());
				viewstate.setText(listPic.get(position).getPicState());
				viewparty.setText(listPic.get(position).getPicParty());
				viewposition.setText(listPic.get(position).getPicPosition());
				viewconstituency.setText(listPic.get(position).getPicConstituency());


				searchEdt = (EditText)mView.findViewById(R.id.serach_edt);
				Log.d("Error","newcheck");
				searchEdt.addTextChangedListener(new TextWatcher()
				{
					public void afterTextChanged(Editable s) 
					{
						String text = searchEdt.getText().toString().toLowerCase();
						adapter.filter(text);
					}
					public void beforeTextChanged(CharSequence s, int start, int count, int after)
					{
					}
					public void onTextChanged(CharSequence s, int start, int before, int count)
					{
					}
				});	
			}
		});
		
		Log.d("ERRRRROORR","BUTTON PRESSED");
		Button commnt = (Button) mView.findViewById(R.id.button1);
		Log.d("ERRRRROORR","BUTTON PRESSED2");
//		commnt.setOnClickListener(new OnClickListener() {

//			@Override
//			public void onClick(View v) {
				// TODO Auto-generated method stub
///				Log.d("ERRRRROORR","BUTTON PRESSED3");
//				Intent intent = new Intent(mView.getContext(), ViewComment.class);
//				intent.putExtra("Id", listPic.get(position).getPicId());
//				intent.putExtra("name", listPic.get(position).getPicName());
//				startActivity(intent);

	//		}
	//	});
		
		viewpic = (ImageView)mView.findViewById(R.id.pic3);
		viewparty = (TextView)mView.findViewById(R.id.party);
		viewname = (TextView)mView.findViewById(R.id.name);
		viewstate = (TextView)mView.findViewById(R.id.state);
		viewposition = (TextView)mView.findViewById(R.id.position);
		viewconstituency = (TextView)mView.findViewById(R.id.constituency);
		return mView;
	}
	public boolean onKey(int keyCode, KeyEvent event) 
	{
		if ((keyCode == KeyEvent.KEYCODE_BACK) ) 
		{
			int screen = fliper.getDisplayedChild();

			if (screen == VIEW_PIC_SCREEN) 
			{
				Sliding.slideFromLeftToRight(LIST_PIC_SCREEN, fliper);
				return true;
			}
		}
		return false;

	}

	@Override
	public void onItemClick(AdapterView<?> arg0, View arg1, int arg2,long arg3) 
	{
		// TODO Auto-generated method stub

	}

	@Override
	public void afterTextChanged(Editable arg0) 
	{
		// TODO Auto-generated method stub

	}

	@Override
	public void beforeTextChanged(CharSequence arg0, int arg1, int arg2,int arg3) 
	{
		// TODO Auto-generated method stub

	}

	@Override
	public void onTextChanged(CharSequence arg0, int arg1, int arg2,int arg3) 
	{
		// TODO Auto-generated method stub

	}
}


