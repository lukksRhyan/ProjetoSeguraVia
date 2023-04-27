package dados;

public class Local {
	private String UF;
	private Coordenada coord;
	
	Local(String UF, Coordenada coord){
		this.UF = UF;
		this.coord = coord;
	}
}
class Coordenada{
	float longitude;
	float latitude;
	
	Coordenada(float longitude, float latitude){
		this.longitude = longitude;
		this.latitude = latitude;
	}
}
