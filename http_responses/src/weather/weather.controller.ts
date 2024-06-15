import { Controller, Get, Param, Query, Res } from '@nestjs/common';
import { WeatherService } from './weather.service';
import { Response } from 'express';

@Controller('weather')
export class WeatherController {
    constructor(private readonly weatherService: WeatherService){}


    @Get()
    async getWeather(@Query('city') city: string, @Res() res: Response){
        if(!city){
            return res.status(400).json({ message: 'City parameter is required' });
        }
        
        try{
            const weatherData = await this.weatherService.getWeather(city);
            res.status(200).json(weatherData);
        }
        catch (error) {
            res.status(error.getStatus()).json({ message: error.message });
        }
    }


}
