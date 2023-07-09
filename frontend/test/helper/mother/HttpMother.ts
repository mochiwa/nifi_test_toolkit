import {HttpErrorResponse, HttpHeaders, HttpResponse} from "@angular/common/http";


export class HttpMother {

  public static default({code = 200}, body = {}): HttpResponse<any> {
    return new HttpResponse({
      headers: new HttpHeaders({
        code: code
      }),
      body: body
    });
  }

  public static error({
                        errors = null,
                        headers = new HttpHeaders({}),
                        status = 400,
                        statusText = "httpErrorMock",
                        url = "localhost"
                      } = {}): any {
    const error = new HttpErrorResponse({
      error: errors,
      headers: headers,
      status: status,
      statusText: statusText,
      url: url
    })
    return JSON.parse(JSON.stringify(error))
  }
}
