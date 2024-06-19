import { HttpException, Injectable, HttpStatus } from '@nestjs/common';
import axios from 'axios';

@Injectable()
export class WeatherService {
    private readonly OPEAN_WEATHER_API_KEY = process.env.OPEAN_WEATHER_API_KEY;


    async getWeather(city: string): Promise<any>{
        const url = `https://api.openweathermap.org/data/2.5/weather?q=${city}&appid=${this.OPEAN_WEATHER_API_KEY}`;
        
        try{
            const response = await axios.get(url);
            return response.data;
        }
        catch(error){
            if (error.response){
                throw new HttpException(error.response.statusText, error.response.status)
            }
            else {
                throw new HttpException('Server error', HttpStatus.INTERNAL_SERVER_ERROR);
              }
        }
    }


}
