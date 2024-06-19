import { Controller, Get, HttpCode, Param, Post, Query, Redirect, Res } from '@nestjs/common';
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
        
        // const tmp = null;
        // const error = tmp.toString(); // error to get 500 status code
        
        // if uncomment this part we will get 500s status code
        
        // if we change some letter in the url it return 400s status code

        // if we go to this url we will get 200s

        try{
            const weatherData = await this.weatherService.getWeather(city);
            res.status(200).json(weatherData);
        }
        catch (error) {
            res.status(error.getStatus()).json({ message: error.message });
        }
    }

    @Get('redirect')
    @Redirect('https://www.google.com/', 302)
    async redirect(@Query('redirect') redirect: string, res: Response){
        
        // if we use this method we will get 300s status, but we can see it only in 
        // developer tools of browser, because we will be redirected instantly
        // and will see 200s code on the redirected page 
        
        if (redirect){
            return {url: redirect, statuscode: 301};
        }
    }

    @Get('continue')
    async continue(@Res() res: Response) {
        
        // if we go to this url we theoretical will see 100s
        // but as I anderstood browser is whaiting while we
        // will some data... 

        return res.status(100).json({message: 'something'});
    }

}


