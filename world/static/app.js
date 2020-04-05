import L  from 'leaflet'
require('leaflet-css')
import $ from 'jquery' 
import Backbone from 'backbone'
import _ from 'underscore'

const apiUrl = '/api/v1/'
const iconsUrl = '/static/icons/'


class Country extends Backbone.Model {
    initialize() {
        this.url = apiUrl+'country/'
    }
}


class Countries extends Backbone.Collection {
    initialize(options) {
        this.url = apiUrl+'country/'
        this.model = Country
    }    
}


class Town extends Backbone.Model {
    initialize() {
        this.url = apiUrl+'town/'    
    }    
}


class Towns extends Backbone.Collection {

    initialize(options) {
        this.url = apiUrl+'town/'
        this.model = Town
    }
}


class CountryView  extends Backbone.View {
    constructor(options) {  
        super(options)    
    }    

    initialize(options) {
        this.map_obj= options.map_obj
        this.model = options.model
    }

    get_icon() {
        return L.icon({
            iconUrl: iconsUrl+'country.png', 
            iconSize:     [24, 24], 
            iconAnchor:   [12, 12],
            popupAnchor:  [0, 24] 
        })
    }

    render () {
        L.marker(
            new L.latLng(this.model.get('center').coordinates[1],this.model.get('center').coordinates[0]),
            {
                icon: this.get_icon()
            }
            ).bindPopup(
                '<b>name:</b>'+this.model.get('name')+'<br />' +
                '<b>area:</b>'+this.model.get('area')+'<br />' + 
                '<b>pop2005:</b>'+this.model.get('pop2005')+'<br />' + 
                '<b>fips:</b>'+this.model.get('fips')+'<br />' + 
                '<b>iso2:</b>'+this.model.get('iso2')+'<br />' + 
                '<b>iso3:</b>'+this.model.get('iso3')+'<br />' + 
                '<b>un:</b>'+this.model.get('un')+'<br />' + 
                '<b>region:</b>'+this.model.get('region')+'<br />' + 
                '<b>subregion:</b>'+this.model.get('subregion')+'<br />'
            ).addTo(
                this.map_obj
            )
    }
}


class TownView  extends Backbone.View {
    constructor(options) {  
        super(options)    
    }    

    initialize(options) {
        this.map_obj= options.map_obj
        this.model = options.model
                
    }

    get_icon() {
        return L.icon({
            iconUrl: iconsUrl+'town.png', 
            iconSize:     [24, 24], 
            iconAnchor:   [12, 12],
            popupAnchor:  [0, 24] 
        })
    }

    render () {
        L.marker(
            new L.latLng(this.model.get('center').coordinates[1],this.model.get('center').coordinates[0]),
            {
                icon: this.get_icon()
            }
            ).bindPopup(
                '<b>name:</b>'+this.model.get('name')+'<br />' +
                '<b>asciiname:</b>'+this.model.get('asciiname')+'<br />' + 
                '<b>population:</b>'+this.model.get('population')+'<br />' + 
                '<b>timezone:</b>'+this.model.get('timezone')+'<br />' + 
                '<b>geonameid:</b>'+this.model.get('geonameid')+'<br />' + 
                '<b>admin2_code:</b>'+this.model.get('admin2_code')+'<br />' + 
                '<b>admin3_code:</b>'+this.model.get('admin3_code')+'<br />' + 
                '<b>admin4_code:</b>'+this.model.get('admin4_code')+'<br />' + 
                '<b>cc2:</b>'+this.model.get('cc2')+'<br />' + 
                '<b>country_code:</b>'+this.model.get('country_code')+'<br />' + 
                '<b>elevation:</b>'+this.model.get('elevation')+'( dem: '+this.model.get('dem')+')<br />' + 
                '<b>feature_class:</b>'+this.model.get('feature_class')+'<br />' + 
                '<b>feature_code:</b>'+this.model.get('feature_code')+'<br />' + 
                '<b>is capital:</b>'+(this.model.get('is_capital') ? 'YES':'NO')+'<br />' + 
                '<b>modification_date:</b>'+this.model.get('modification_date')+'<br />' 
            ).addTo(
                this.map_obj
            )
    }
}


class AppView extends Backbone.View {
    constructor(options) {  
        super(options)    
    }    

    initialize(options) {
       this.create_map()
       // Get Countries
       this.countries = new Countries()
       this.countries.on('reset', this.render_countries, this)
       this.countries.fetch({ reset: true })
       // Town
       this.towns = new Towns()
       this.towns.on('reset', this. render_towns, this)
       this.towns.fetch({ reset: true })
    }  

    create_map()
    {
        this.map_obj = L.map(this.el).setView([50,50], 2)
        L.tileLayer(
                   'http://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png',
                    {
                        attribution: '&copy; ' +'<a href="http://openstreetmap.org">OpenStreetMap</a>' + ' Contributors',
                    maxZoom: 19,
                    }
        ).addTo(
            this.map_obj
        )
    }

    render_countries()
    {
        this.countries.forEach( (item) =>  {
            const itemView = new CountryView({
                model: item,
                map_obj: this.map_obj
            })
            itemView.render()
        })
    }

    render_towns()
    {
        this.towns.forEach( (item) =>  {
            const itemView = new TownView({
                model: item,
                map_obj: this.map_obj
            })
            itemView.render()
        })
    }

    render () {
    }
}


const view = new AppView({
    el: 'app',
});