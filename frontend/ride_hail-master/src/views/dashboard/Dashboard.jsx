import React from 'react';
import { Component} from "react";
import {Map, GoogleApiWrapper} from "google-maps-react";


function Dashboard() {
     class MapContainer extends Component {
        render() {
            return (
                <div>
                    <Map
                        google={this.props.google}
                        zoom={10}
                        style={
                            {
                                width: '100%',
                                height: '100%'
                            }
                        }
                        initialCenter={{ lat: 6.5244, lng: 3.3792}}
                    />
                </div>

            );
        }
    }




export default GoogleApiWrapper({
    apiKey:"518735243715-r53rfi4qnqvfjo93uur7823t7278s9mv.apps.googleusercontent.com"
})
(MapContainer)}
// export default Dashboard;