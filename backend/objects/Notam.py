import json

class Notam:
    def __init__(self, notam_string):
        # Parse the input NOTAM JSON string and initialize the instance variables
        notam_data = json.loads(notam_string)
        core_data = notam_data['properties']['coreNOTAMData']['notam']

        # Initialize all the specified attributes
        self.account_id = core_data.get('accountId', None)
        self.affected_fir = core_data.get('affectedFIR', None)
        self.classification = core_data.get('classification', None)
        self.effective_start = core_data.get('effectiveStart', None)
        self.effective_end = core_data.get('effectiveEnd', None)
        self.icao_location = core_data.get('icaoLocation', None)
        self.id = core_data.get('id', None)
        self.issued = core_data.get('issued', None)
        self.last_updated = core_data.get('lastUpdated', None)
        self.location = core_data.get('location', None)
        self.maximum_fl = core_data.get('maximumFL', None)
        self.minimum_fl = core_data.get('minimumFL', None)
        self.number = core_data.get('number', None)
        self.purpose = core_data.get('purpose', None) 
        self.scope = core_data.get('scope', None)     
        self.selection_code = core_data.get('selectionCode', None)
        self.series = core_data.get('series', None)
        self.traffic = core_data.get('traffic', None)  
        self.type = core_data.get('type', None)

        # Text might not have a default in the original JSON, so consider handling it if needed.
        self.text = core_data.get('text', None)

    def __eq__(self, other):
        if isinstance(other, Notam):
            return self.id == other.id
        return False
    
    def __hash__(self):
        return hash(self.id)

    def jsonify_notam(self):
        # Return a dictionary representation of the Notam instance
        return {
            'account_id': self.account_id,
            'affected_fir': self.affected_fir,
            'classification': self.classification,
            'effective_start': self.effective_start,
            'effective_end': self.effective_end,
            'icao_location': self.icao_location,
            'id': self.id,
            'issued': self.issued,
            'last_updated': self.last_updated,
            'location': self.location,
            'maximum_fl': self.maximum_fl,
            'minimum_fl': self.minimum_fl,
            'number': self.number,
            'purpose': self.purpose,            
            'scope': self.scope,               
            'selection_code': self.selection_code,
            'series': self.series,
            'traffic': self.traffic,           
            'type': self.type,
            'text': self.text                  
        }

    def __repr__(self):
        return f"Notam(ID: {self.id}, Series: {self.series}, ICAO: {self.icao_location})"
