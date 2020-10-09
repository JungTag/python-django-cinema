#include "studio.h"

int main()
{
    FILE *pFile = NULL;
    errno_t err;
    int count;
    unsigned int data;
  unsigned int data1 = 0xAABBCCDD;
  unsigned int data2 = 0x11223344;

  err = fopen_s(&pFile, "test.bin", "wb");
  if (err) {
    printf("Cannot open file\n");
    return 1;
  }
  fwrite(&data1, sizeof(data1), 1, pFile);
  fwrite(&data2, sizeof(data2), 1, pFile);
  fclose(pFile);

err = fopen_s(&pFile, "test.bin", "rb");
  if (err) {
    printf("Cannot open file\n");
    return 1;
  }

  while (1) {
    count = fread(&data, sizeof(data1), 1, pFile);
    if (count  != 1)
      break;
    printf("%8x\n", data);
  }
  fclose(pFile);

  return 0;
}

}