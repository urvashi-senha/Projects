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

public class ManifestoAdapter extends BaseAdapter {
	private Context mContext;
	private LayoutInflater mInflater;
	private List<Manifesto> picList = null;
	private ArrayList<Manifesto> listpicOrigin;

	public ManifestoAdapter(Context context, List<Manifesto> picList) {
		mContext = context;
		this.picList = picList;
		mInflater = LayoutInflater.from(mContext);
		this.listpicOrigin = new ArrayList<Manifesto>();
		this.listpicOrigin.addAll(picList);
		Log.d("Error","piclistorigin added");
	}

	public class ViewHolder {
		
		TextView picPolitician;
		TextView picContent;
		TextView picHas_done;
		
	}

	public View getView(int position, View view, ViewGroup parent) {
		Log.d("Error","here1");
		final ViewHolder holder;
		if (view == null) {
			Log.d("Error","here21");
			holder = new ViewHolder();
			view = mInflater.inflate(R.layout.list_item2, null);
			holder.picPolitician = (TextView) view.findViewById(R.id.pic_pol_txt);
			Log.d("Error","here22");
			holder.picContent = (TextView) view.findViewById(R.id.pic_con_txt);
			Log.d("Error","here23");
			holder.picHas_done = (TextView) view.findViewById(R.id.pic_hd_txt);
			view.setTag(holder);
		} else {
			Log.d("Error","here3");
			holder = (ViewHolder) view.getTag();
		}
		Log.d("Error","here4");
		holder.picPolitician.setText(picList.get(position).getpicPolitician());
		holder.picContent.setText(picList.get(position).getpicContent());
		holder.picHas_done.setText(picList.get(position).getpicHas_done());
		Log.d("Error","here5");
		return view;
	}

	public int getCount() {
		return picList.size();
	}

	public Manifesto getItem(int position) {
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
	

}