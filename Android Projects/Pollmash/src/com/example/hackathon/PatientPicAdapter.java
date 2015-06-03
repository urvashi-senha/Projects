package com.example.hackathon;

import java.util.ArrayList;
import java.util.List;



import android.os.Bundle;
import android.app.Activity;
import android.content.Context;
import android.util.Log;
import android.view.LayoutInflater;
import android.view.Menu;
import android.view.View;
import android.view.ViewGroup;
import android.widget.BaseAdapter;
import android.widget.ImageView;
import android.widget.TextView;

public class PatientPicAdapter extends BaseAdapter {
	private Context mContext;
	private LayoutInflater mInflater;
	private List<Patient> picList = null;
	private ArrayList<Patient> listpicOrigin;

	public PatientPicAdapter(Context context, List<Patient> picList) {
		mContext = context;
		this.picList = picList;
		mInflater = LayoutInflater.from(mContext);
		this.listpicOrigin = new ArrayList<Patient>();
		this.listpicOrigin.addAll(picList);
		Log.d("Error","piclistorigin added");
	}

	public class ViewHolder {
		
		TextView picName;
		TextView picConstituency;
		TextView picParty;
	}

	public View getView(int position, View view, ViewGroup parent) {
		Log.d("Error","here1");
		final ViewHolder holder;
		if (view == null) {
			Log.d("Error","here21");
			holder = new ViewHolder();
			view = mInflater.inflate(R.layout.list_item, null);
			holder.picName = (TextView) view.findViewById(R.id.pic_name_txt);
			Log.d("Error","here22");
			holder.picConstituency = (TextView) view.findViewById(R.id.pic_constituency_txt);
			Log.d("Error","here23");
			holder.picParty = (TextView) view.findViewById(R.id.pic_party_txt);
			view.setTag(holder);
		} else {
			Log.d("Error","here3");
			holder = (ViewHolder) view.getTag();
		}
		Log.d("Error","here4");
		holder.picName.setText(picList.get(position).getPicName());
		holder.picConstituency.setText(picList.get(position).getPicConstituency());
		holder.picParty.setText(picList.get(position).getPicParty());
		Log.d("Error","here5");
		return view;
	}

	public int getCount() {
		return picList.size();
	}

	public Patient getItem(int position) {
		return picList.get(position);
	}

	public long getItemId(int position) {
		return position;
	}

	/**
	 * Filter
	 * @author 9Android.net
	 * 
	 */
	public void filter(String charText) {
		charText = charText.toLowerCase();
		picList.clear();
		if (charText.length() == 0) {
			picList.addAll(listpicOrigin);
		} else {
			for (Patient pic : listpicOrigin) {
				if (pic.getPicConstituency().toLowerCase().contains(charText)) {
					picList.add(pic);
				}
			}
		}
		notifyDataSetChanged();
	}

}