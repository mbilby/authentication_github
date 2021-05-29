  <center><img src="https://user-images.githubusercontent.com/51273322/120051058-2c84ff00-bfed-11eb-92e5-cd7116b55d3d.png" width="80%" /></center>
  <center>
    <h1>Autenticação GitHub via API com Python</h1>
  </center>
  <h1>Criar um token de acesso pessoal</h1>
  <p>Você deve criar um token de acesso pessoal para usar no lugar de uma senha
    com a linha de comando ou com a API.</p>
<div>
    <div>
      <p>Os tokens de acesso pessoal (PATs) são uma alternativa para o uso de
        senhas para autenticação no GitHub ao usar a API do GitHub ou a linha
        de comando.</p>
    </div>
    <div>
      <p>Se você deseja usar um PAT para acessar recursos pertencentes a uma
        organização que usa SAML SSO, você deve autorizar o PAT. Para mais
        informações consulte "Sobre autenticação com logon único SAML" e "
        Autorizando um token de acesso pessoal para uso com logon único
        SAML.</p>
    </div>
    <div>
      <p>Como medida de segurança, o GitHub remove automaticamente tokens de
        acesso pessoal que foram usados em um ano.</p>
    </div>
     <div>
      <p>Se você deseja usar um PAT para acessar recursos pertencentes a uma
        organização que usa SAML SSO, você deve autorizar o PAT. Para mais
        informações consulte "Sobre autenticação com logon único SAML" e "
        Autorizando um token de acesso pessoal para uso com logon único
        SAML.</p>
    </div>
    <div>
      <p>Como medida de segurança, o GitHub remove automaticamente tokens de
        acesso pessoal que foram usados em um ano.</p>
    </div>
</div>
  <div>
    <div>
      <h3>Criar um Token</h3>
      <ol>
        <li>
          <p>
            <a
              href="https://docs.github.com/pt/github/getting-started-with-github/signing-up-for-github/verifying-your-email-address">Verifique
              seu endereço de e-mail</a>
            caso não tenha verificado.
          </p>
        </li>
        <li>
          <p>No canto superior direito de qualquer página, clique na sua foto de
            perfil e, em seguida, clique em <strong>Configurações</strong>.
          </p>
          <span>
            <img src="https://docs.github.com/assets/images/help/settings/userbar-account-settings.png" width="15%">
          </span>
        </li>
        <li>
          <p>Na barra lateral esquerda, clique em <strong>Developer settings</strong>(Configurações do desenvolvedor).
          </p>
          <span>
            <img src="https://docs.github.com/assets/images/help/settings/developer-settings.png" width="15%">
          </span>
        </li>
        <li>
          <p>Na barra lateral esquerda, clique em <strong> tokens de acesso pessoal</strong>. </p>
        </li>
        <li>
          <p>Clique em <strong>Generate new token</strong> (Gerar novo token). </p>]
          <span>
            <img src="https://docs.github.com/assets/images/help/settings/generate_new_token.png" width="45%">
          </span>
        </li>
        <li>
          <p>Dê ao seu token um nome descritivo.</p>
          <span>
            <img src="https://docs.github.com/assets/images/help/settings/token_description.png" width="35%">
          </span>
        </li>
        <li>
          <p>Selecione os escopos, ou as permissões, aos quais deseja conceder esse token. Para usar seu token para
            acessar repositórios da linha de comando, selecione <strong>repo</strong>.</p>
          <span>
            <img src="https://docs.github.com/assets/images/help/settings/token_scopes.gif" width="50%">
          </span>
        </li>
        <li>
          <p>Clique em <strong>Generate token</strong> (Gerar token). </p>
          <span>
            <img src="https://docs.github.com/assets/images/help/settings/generate_token.png" width="20%">
          </span>
        </li>
      </ol>
    </div>
    <div>
      <h1>Autenticação com Personal Token</h1>
      <p>
        A Personal Token e Basic Autentication são praticamente iguais, as duas
        necessitam do username como campo, mas a primeira forma usar um token
        que é criado na página de configurações do usuário e a segunda usa a
        própria senha do dele.
      </p>
    </div>
    <div>
      <h1>Personal Token</h1>
      <span>
        <img src="https://user-images.githubusercontent.com/51273322/120053111-70303680-bff6-11eb-9f68-968e0e9a7cdc.png" width="30%">
      </span>
      <h1>Função que irá realizar a autenticação e mostrar os dados do usuário</h1>
      <span>
        <img src="https://user-images.githubusercontent.com/51273322/120053118-74f4ea80-bff6-11eb-809c-b9ebce17da63.png" width="30%">
      </span>
      <h1>Em seguida basta chamar a Função</h1>
      <span>
        <img src="https://user-images.githubusercontent.com/51273322/120053119-758d8100-bff6-11eb-8031-6b12f77b6f99.png" width="20%">
      </span>
  </div>
  
