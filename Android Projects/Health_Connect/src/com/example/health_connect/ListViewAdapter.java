package com.example.health_connect;

import java.util.ArrayList;
import java.util.List;

import android.content.Context;
import android.content.Intent;
import android.util.Log;
import android.view.LayoutInflater;
import android.view.View;
import android.view.View.OnClickListener;
import android.view.ViewGroup;
import android.widget.BaseAdapter;
import android.widget.ImageView;
import android.widget.TextView;

public class ListViewAdapter extends BaseAdapter{
	    Context context;
	    LayoutInflater inflater;
	    ImageLoader imageLoader;
	    private List<Report> report_list = null;
	    private ArrayList<Report> arraylist;
	    
	    public ListViewAdapter(Context context,
	            List<Report> report_list) {
	        this.context = context;
	        this.report_list = report_list;
	        inflater = LayoutInflater.from(context);
	        this.arraylist = new ArrayList<Report>();
	        this.arraylist.addAll(report_list);
	        imageLoader = new ImageLoader(context);
	        
	    }
	    public class ViewHolder {
	        TextView heading;
	        TextView subject; 
	        ImageView image;
	    }
		@Override
		public int getCount() {
			// TODO Auto-generated method stub
			return report_list.size();
		}
		@Override
		public Object getItem(int position) {
			// TODO Auto-generated method stub
			return report_list.get(position);
		}
		@Override
		public long getItemId(int position) {
			// TODO Auto-generated method stub
			return position ;
		}
		@Override
		public View getView(final int position, View view, ViewGroup parent) {
			// TODO Auto-generated method stub
			final ViewHolder holder;
	        if (view == null) {
	            holder = new ViewHolder();
	            view = inflater.inflate(R.layout.list_view, null);
	            // Locate the TextViews in listview_item.xml
	            holder.heading = (TextView) view.findViewById(R.id.headtxt);
	            holder.subject = (TextView) view.findViewById(R.id.subtxt);
	            // Locate the ImageView in listview_item.xml
	            holder.image = (ImageView) view.findViewById(R.id.imag);
	            view.setTag(holder);
	            Log.d("Check6", "here it is in list adapter");
	        } 
	        else {
	            holder = (ViewHolder) view.getTag();
		}
	        holder.heading.setText(report_list.get(position).getHead());
	        holder.subject.setText(report_list.get(position).getSub());
	        imageLoader.DisplayImage(report_list.get(position).getImag(),
	                holder.image); 
		
		view.setOnClickListener(new OnClickListener() {
			 
            public void onClick(View arg0) {
                // Send single item click data to SingleItemView Class
            	Log.d("check10","single class starting");
            	Intent intent = new Intent(context, SingleItemView.class);
 
                intent.putExtra("heading",
                        (report_list.get(position).getHead()));
                
                intent.putExtra("subject",
                        (report_list.get(position).getSub()));
               
                intent.putExtra("image",
                        (report_list.get(position).getImag()));
                // Start SingleItemView Class
                Log.d("Check7", "starting intent");
                context.startActivity(intent);
            }
        });
		Log.d("Check7", "returning view");
        return view;
		}
}
