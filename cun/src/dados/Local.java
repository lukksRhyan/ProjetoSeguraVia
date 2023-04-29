package dados;

public class Local {
	private Rodovia BR;
	private String UF;
	private Coordenada KM;
	
	Local(String UF, Rodovia BR, int Kilometro){
		this.UF = UF;
		this.BR = BR;
		this.KM = BR[Kilometro];
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
class Rodovia{//com ajuda do Python é possivel guardar as rodovias como uma lista de coordenadas
	private Coordenada[] KM;
	Rodovia(){
		this(0);
	}
	Rodovia(int comprimento){
		this.km = new Coordenada[comprimento];
		for(int i = 0;i<comprimento; i++){
			this.km[i] = new Coordenada();//Tem que ver como que eu salvo como corrdenada cada km de uma rodovia
	 
		}
	}
	public Coordenada coordKM(int KM){
		try{
			return this[KM];
		}catch(ArrayIndexOutOfBounds exception e){
			System.out.println("Kilometro inexistente na rodovia atual");
		}
	}
}
