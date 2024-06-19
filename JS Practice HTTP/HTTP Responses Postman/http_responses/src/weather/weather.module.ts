import { Module } from '@nestjs/common';
import { WeatherService } from './weather.service';
import { WeatherController } from './weather.controller';
import { ConfigModule } from '@nestjs/config';

@Module({
  providers: [WeatherService],
  controllers: [WeatherController],
  
})
export class WeatherModule {}
