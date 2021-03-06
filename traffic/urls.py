from django.conf.urls import url
from traffic import views, authen_view
from backend import crash_view, parking_view, weather_view, DNL_view
from django.contrib.auth import views as django_auth_views

urlpatterns = [
    url(r'^$', views.index, name='index'),

    url(r'^camera/$', views.camera, name='camera'),
    url(r'^ajaxtest/$',views.ajaxtest, name='ajaxtest'),

    url(r'^count/$', views.count, name='count'),

#++++++++++++++++++++++++++++++++++++++++++++++++ Weather +++++++++++++++++++++++++++++++++++++++
    #url(r'^weather/$', views.weather, name='weather'),
    #url(r'^get_county_weather/$', views.get_county_weather, name = 'get_county_weather'),
    #url(r'^get_weather/$', views.get_weather, name = 'get_weather'),

    # zipcode area weather
    url(r'^weather/$', weather_view.weather, name='weather'),
    url(r'^get_zipcode_areas/$', weather_view.get_zipcode_areas, name = 'get_zipcode_areas'),
    url(r'^get_weather/$', weather_view.get_weather, name = 'get_weather'),
#++++++++++++++++++++++++++++++++++++++++++++++++ Weather_end +++++++++++++++++++++++++++++++++++++++


    url(r'^ev_stations/$', views.ev_stations, name='ev_stations'),

#++++++++++++++++++++++++++++++++++++++++++++++++ Congestion(Max) +++++++++++++++++++++++++++++++++++++++
    url(r'^congestion_task_request/$', views.congestion_task_request, name='congestion_task_request'),
    url(r'^congestion_task_view/$', views.congestion_task_view, name='congestion_task_view'),
    url(r'^get_links/$', views.get_links, name='get_links'),
    url(r'^submit_link_update/$', DNL_view.submit_link_update, name='submit_link_update'),
    url(r'^get_tasks/$', DNL_view.get_tasks, name='get_tasks'),
    url(r'^delete_task/$', DNL_view.delete_task, name='delete_task'),
    url(r'^get_parameter/$', DNL_view.get_parameter, name='get_parameter'),
    url(r'^get_congestion/$', DNL_view.get_congestion, name='get_congestion'),
    url(r'^get_congestion_for_link/$', DNL_view.get_congestion_for_link, name='get_congestion_for_link'),
    url(r'^congestion_online/$', DNL_view.congestion_online, name='congestion_online'),
    url(r'^get_DMS/$', DNL_view.get_DMS, name='get_DMS'),
    url(r'^get_online_congestion/$', DNL_view.get_online_congestion, name='get_online_congestion'),
    url(r'^get_latest_online_time/$', DNL_view.get_latest_online_time, name='get_latest_online_time'),
    url(r'^get_real_time_VMS/$', DNL_view.get_real_time_VMS, name='get_real_time_VMS'),
    url(r'^submit_link_update_online/$', DNL_view.submit_link_update_online, name='submit_link_update_online'),



    url(r'^demo_congestion_task_request/$', views.demo_congestion_task_request, name='demo_congestion_task_request'),
    url(r'^demo_congestion_task_view/$', views.demo_congestion_task_view, name='demo_congestion_task_view'),
    url(r'^demo_request_response/$', views.demo_request_response, name='demo_request_response'),
    url(r'^demo_congestion_task_list/$', views.demo_congestion_task_list, name='demo_congestion_task_list'),
    url(r'^demo_index/$', views.demo_index, name='demo_index'),



    # +++++++++++++++++++++++++++++++++++++++++++++++++++++++++  Travel  +++++++++++++++++++++++++++++++++++++++++++++++++++++++
    url(r'^travel_time/$', views.travel_time, name='travel_time'),
    url(r'^travel_time_new/$', views.travel_time_new, name='travel_time_new'),
    url(r'^get_node_info_for_one_corridor/$', views.get_node_info, name='get_node_info'),
    url(r'^get_spc_traveltime/$', views.get_spctraveltime, name='get_spctraveltime'),
    url(r'^get_spc_traveltimeformanyyears/$', views.get_spctraveltimeformanyyears, name='get_spctraveltimeformanyyears'),
    url(r'^get_spc_years/$', views.get_spcyears, name='get_spcyears'),
    url(r'^travel_time_corridorafter2013/$', views.travel_time_corridorafter2013, name='travel_time_corridorafter2013'),
    url(r'^get_node_info_2013to2015/$', views.get_node_info_2013to2015, name='get_node_info_2013to2015'),
    url(r'^get_spc_traveltime_2013to2015/$', views.get_spctraveltime_2013to2015, name='get_spctraveltime2013to2015'),
    url(r'^get_travel_time/$', views.get_travel_time, name='get_travel_time'),
    url(r'^get_travel_time_prediction/$', views.get_travel_time_prediction, name='get_travel_time_prediction'),
    url(r'^get_road_tmc/$', views.get_road_tmc, name='get_road_tmc'),
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++  END  ++++++++++++++++++++++++++++++++++++++++++++++++++++++++


# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++  Transit  +++++++++++++++++++++++++++++++++++++++++++++++++++++++
    url(r'^get_route/$', views.get_route, name='get_route'),
    url(r'^get_stops/$', views.get_stops, name='get_stops'),
    url(r'^get_trips/$', views.get_trips, name='get_trips'),
    url(r'^transit_data/$', views.transit_data, name='transit_data'),
    url(r'^get_stop_routes/$', views.get_stop_routes, name='get_stop_route'),

    url(r'^transit_ontimeperformance_byroute/$', views.transit_ontimeperformance_byroute, name='transit_ontimeperformance_byroute'),
    url(r'^transit_ontimeperformance_bystop/$', views.transit_ontimeperformance_bystop, name='transit_ontimeperformance_bystop'),
    url(r'^transit_schedule/$', views.transit_schedule, name='transit_schedule'),
    url(r'^transit_waitingtime_byroute/$', views.transit_waitingtime_byroute, name='transit_waitingtime_byroute'),
    url(r'^transit_waitingtime_bystop/$', views.transit_waitingtime_bystop, name='transit_waitingtime_bystop'),
    url(r'^transit_waitingtime_byOD/$', views.transit_waitingtime_byOD, name='transit_waitingtime_byOD'),
    url(r'^transit_stopskipping/$', views.transit_stopskipping, name='transit_stopskipping'),
    url(r'^transit_crowding/$', views.transit_crowding, name='transit_crowding'),
    url(r'^transit_crowding_heatmap/$', views.transit_crowding_hm, name='transit_crowding_hm'),
    url(r'^transit_busbunching/$', views.transit_bunching, name='transit_busbunching'),
    url(r'^transit_busbunching_heatmap/$', views.transit_bunching_hm, name='transit_busbunching_hm'),
    url(r'^transit_bustraveltime/$', views.transit_bustraveltime, name='transit_bustraveltime'),

    url(r'^transit_metrics_op_byroute/$', views.transit_metrics_op_byroute, name='transit_metrics_op_byroute'),
    url(r'^transit_metrics_op_bystop/$', views.transit_metrics_op_bystop, name='transit_metrics_op_bystop'),
    url(r'^transit_metrics_schedule_opt/$', views.transit_metrics_schedule_opt, name='transit_metrics_schedule_opt'),

    url(r'^transit_metrics_wt_byroute/$', views.transit_metrics_wt_byroute, name='transit_metrics_wt_byroute'),
    url(r'^transit_metrics_wt_bystop/$', views.transit_metrics_wt_bystop, name='transit_metrics_wt_bystop'),
    url(r'^transit_metrics_wt_byOD/$', views.transit_metrics_wt_byOD, name='transit_metrics_wt_byOD'),

    url(r'^transit_metrics_stopskipping/$', views.transit_metrics_stopskipping, name='transit_metrics_stopskipping'),

    url(r'^transit_metrics_crowding/$', views.transit_metrics_crowding, name='transit_metrics_crowding'),

    url(r'^transit_metrics_bunching/$', views.transit_metrics_bunching, name='transit_metrics_bunching'),

    url(r'^transit_metrics_bustraveltime/$', views.transit_metrics_bustraveltime, name='transit_metrics_bustraveltime'),

    url(r'^bus_real_time/$', views.bus_real_time, name='bus_real_time'),
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++  End  ++++++++++++++++++++++++++++++++++++++++++++++++++++++++


# ~~~~~~~~~~~~~~~~~~~~~~~~ start Yiming ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    url(r'^twitter_map/$', views.twitter_map, name='twitter_map'),
    url(r'^get_incidents_twitter/$', views.get_incidents_twitter, name='get_incidents_twitter'),
    url(r'^get_RT_incidents_twitter/$', views.get_RT_incidents_twitter, name='get_RT_incidents_twitter'),
    url(r'^update_incidents_twitter/$', views.update_incidents_twitter, name='update_incidents_twitter'),

# ~~~~~~~~~~~~~~~~~~~~~~~~~ end Yiming ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~




    url(r'^incidents/$', views.incidents, name='incidents'),
    url(r'^get_incidents_rcrs/$', views.get_incidents_rcrs, name='get_incidents_rcrs'),

    url(r'^download/$', views.download, name='download'),

    url(r'^routing/$', views.routing, name='routing'),
    url(r'^routing_path/$', views.routing_path, name='routing_path'),

    url(r'^test/$', views.test, name='test'),
    url(r'^get_incidents_rcrs_area/$', views.get_incidents_rcrs_area, name='get_incidents_rcrs_area'),
    url(r'^real_time_incidents_rcrs/$', views.real_time_incidents_rcrs, name='real_time_incidents_rcrs'),
    url(r'^real_time_tmc/$', views.real_time_tmc, name='real_time_tmc'),
    url(r'^real_time_tt/$', views.real_time_tt, name='real_time_tt'),
    url(r'^tmc_gis/$', views.TMC_GIS, name='TMC_GIS'),

    url(r'^devices/$', views.device_render, name='devices'),

#counts
    url(r'^get_sensors_counts/$', views.get_sensors_counts, name='get_sensors_counts'),
    url(r'^get_sensors_links/$', views.get_sensors_links, name='get_sensors_links'),
    url(r'^sensors_counts/$', views.sensors_counts_webpage, name='sensors_counts_webpage'),

#SGYang
    url(r'^road_closure/$', views.closure, name='closure'),
    url(r'^get_road_closure_query/$', views.get_road_closure_query, name='get_road_closure_query'),

    url(r'^parking/$', parking_view.parking, name='parking'),
    url(r'^parking_geoJSON_prediction/$', parking_view.street_parking_geojson_prediction, name='parking_geoJSON_prediction'),
    url(r'^parking_lots/$', parking_view.parking_lots, name='parking_lots'),

    url(r'^crash/$', crash_view.crash, name='crash'),
    url(r'^crash_query/$', crash_view.crash_query, name='crash_query'),

#map_displayer
    url(r'^map_displayer/$', views.map_displayer, name='map_displayer'),

#here_tmc_data
    url(r'^tmc_gis_here/$', views.tmc_gis_here, name = 'tmc_gis_here'),
    url(r'^tmc_data_here/$', views.tmc_data_here, name = 'tmc_data_here'),
    url(r'^tmc_tt_here/$', views.tmc_tt_here, name = 'tmc_tt_here'),

#ritis_here_data (real time)
    url(r'^tmc_gis_ritis/$', views.tmc_gis_ritis, name = 'tmc_gis_ritis'),
    url(r'^tmc_real_time_data_ritis/$', views.tmc_real_time_data_ritis, name = 'tmc_real_time_data_ritis'),
    url(r'^tmc_tt_ritis/$', views.tmc_tt_ritis, name = 'tmc_tt_ritis'),

#authentication and registration
    url(r'^register/$', authen_view.register, name='register'),
    url(r'^login/$', authen_view.user_login, name='login'),
    url(r'^restricted/', authen_view.restricted, name='restricted'),
    url(r'^logout/$', authen_view.user_logout, name='logout'),
    url(r'^change-password/', django_auth_views.password_change, {'post_change_redirect': '/traffic/'}, name='password_change'),
    url(r'^change-password-done/', django_auth_views.password_change_done, name='password_change_done'),
]
