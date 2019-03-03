/*
 * IEEE1451_001.h
 *
 *  Created on: Feb 18, 2019
 *      Author: Russty
 */

#ifndef IEEE1451_001_H_
#define IEEE1451_001_H_

void Segmentation_Init()
void Segmentation_AddChannel(char SensorChannel, int Error)
void Segmentation_WriteNewData(char SensorChannel, double SensorData)
void Segmentation_ReadCurrentSegments(char SensorChannel)
void Segmentation_BeginNewSegment(char SensorChannel)
void Segmentation_SetError(char SensorChannel)


#endif /* IEEE1451_001_H_ */
